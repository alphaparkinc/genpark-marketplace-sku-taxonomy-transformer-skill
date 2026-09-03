class MarketplaceSkuTaxonomyTransformerClient:
    def transform_sku_attributes(self, internal_sku='SKU_JACKET_BLK_M', source_attributes=None, target_marketplace='AMAZON_US'):
        if source_attributes is None:
            source_attributes = {'title': 'Men Thermal Down Winter Jacket', 'color': 'Midnight Black', 'gender': 'Male'}
        return {
            'transformation_id': 'tax_xfm_9918',
            'internal_sku': internal_sku,
            'target_marketplace': target_marketplace,
            'target_category_node_id': '1045830',
            'mapped_attributes': {
                'item_name': 'Men Winter Down Puffer Jacket',
                'color_name': 'Black',
                'department_name': 'mens'
            },
            'feed_schema_valid': True,
            'syndication_feed_url': 'https://feedonomics.taxonomy.genpark.ai/feeds/9918.json'
        }
