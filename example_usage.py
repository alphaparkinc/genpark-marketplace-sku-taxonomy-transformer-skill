from client import MarketplaceSkuTaxonomyTransformerClient

def main():
    client = MarketplaceSkuTaxonomyTransformerClient()
    res = client.transform_sku_attributes('SKU_01', None, 'WALMART_COM')
    print('Marketplace Taxonomy Transformer: ' + res['transformation_id'] + ' (' + res['target_marketplace'] + ')')
    print('Category Node: ' + res['target_category_node_id'] + ' | Valid: ' + str(res['feed_schema_valid']))
    print('Feed URL: ' + res['syndication_feed_url'])

if __name__ == '__main__':
    main()
