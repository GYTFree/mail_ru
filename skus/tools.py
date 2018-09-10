from requests import Session, Request
import time
from skus.models import Client


class ShopSession(object):
    _apiUrl = 'https://mall.my.com/oauth/v2/token'  # mail.ru获取店铺token
    _productUrl = 'https://mall.my.com/merchant/wish/api/v2/product/'  # mail.ru获取店铺产品信息
    _order_url = "https://mall.my.com/merchant/wish/api/v2/order/"  # mail.ru获取order信息
    _sku_url = "https://mall.my.com/merchant/wish/api/v2/variant/"  # mail.ru根据sku获取信息

    def __init__(self, shopName):
        self.shopname = shopName.lower()
        self.data = self.set_attrib()
        self.session = Session()
        self.headers = {}
        self.set_headers()

    def get_attrib(self):
        # value = shopKeys.get(self.shopname.lower().title())
        client = Client.objects.filter(shop=self.shopname).first()

        if client:
            data = {}
            data['shop'] = client.shop
            data['username'] = client.username
            data['password'] = client.password
            data['client_id'] = client.client_id
            data['client_secret'] = client.client_secret
            data['grant_type'] = client.grant_type
            return data
        else:
            return None

    def set_attrib(self):
        return self.get_attrib()

    def get_token(self):
        """获取店铺token令牌
        """
        request = Request('post', self._apiUrl, data=self.data).prepare()
        token = self.session.send(request)
        return token.json()

    def set_headers(self):
        """设置会话连接token身份令牌
        """
        token = self.get_token()
        token = ' '.join([token['token_type'].title(), token['access_token']])
        self.headers['Authorization'] = token
        self.session.headers = self.headers

    def get_skus(self, params):
        """
        传入spu-id 或spu 名称参数，调用api接口获取spu产品信息
        params:dict类型
        params = {'id': 'a559c77a-77d8-4926-abd8-d22bb9c3bb93'} 
                或 {'parent_sku': '10807_Gorki'}
        """
        request = Request('get', self._productUrl,
                          params=params, headers=self.headers).prepare()
        response = self.session.send(request)

        if response.json().get('code') == 0:
            return response
        else:
            spu = list(params.values())
            return None

    def get_order(self, params):
        """
        根据orderId获取订单信息
        :return:
        """
        request = Request('get', self._order_url, params=params, headers=self.headers).prepare()
        response = self.session.send(request)
        if response.json().get('code') == 0:
            response = response.json().get('data').get('Order')
            response['shop_name'] = self.shopname
            return response
        else:
            return None

    def parse_products(self, product):
        """获取spu下的所有sku信息
        @product: spu信息  字典类型
        return: sku 生成器
        """
        sku = {}
        info = product.get('data').get('Product')
        sku['shop_name'] = self.shopname
        sku['data_id'] = info['id']
        sku['name'] = info['name']
        sku['parent_sku'] = info['parent_sku']
        sku['description'] = info['description']
        for variant in info['variants']:
            sku['variant_id'] = variant['Variant']['id']
            sku['sku'] = variant['Variant']['sku']
            sku['color'] = variant['Variant']['color']
            sku['size'] = variant['Variant']['size']
            sku['inventory'] = variant['Variant']['inventory']
            sku['price'] = variant['Variant']['price']
            sku['enabled'] = variant['Variant']['enabled']
            sku['main_image'] = variant['Variant']['main_image']
            sku['all_images'] = ';'.join([image for image in variant['Variant']['all_images'] if image])
            sku['updated_at'] = variant['Variant']['updated_at']
            yield sku

    def get_sku_by_name(self, params):
        """根据sku名称获取sku信息
        :param params: sku名称
        :return: dict{}
        """
        request = Request('get', self._sku_url, params=params, headers=self.headers).prepare()
        response = self.session.send(request)

        if response.json().get('code') == 0:
            response = response.json()
            return response.get('data').get('Variant')
        else:
            return None


class Factory(object):
    """设置返回店铺实例化方法对象
    _shopList:dict类型  
    _shopList = {'Kvantym': ShopSession}
    """

    def __init__(self):
        self._shopList = {}

    def getShop(self, shopname):
        if self._shopList.get(shopname):
            return self._shopList.get(shopname)
        else:
            try:
                self._shopList[shopname] = ShopSession(shopname)
                return ShopSession(shopname)
            except Exception:
                return None
