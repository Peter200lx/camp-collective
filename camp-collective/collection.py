from collections import namedtuple


class Collection:
    """Bandcamp Collection tracking, holds all tracks and albums available to re-download"""
    def __init__(self, amount):
        """Initialize an empty dict for items and set total collection size

        :param amount: Total number of item in collection accourding to bandcamp
        """
        self._items = dict()
        self._amount = amount

    def extend(self, items, download_urls):
        """Update the dictionary of known items in your collection from discord's API

        :param items: list of collection items from bandcamp's website or api
        :param download_urls: dict of sales keys to full urls to re-download item
        :return: None
        """
        for item in items:
            download_url_id = item['sale_item_type'] + \
                              str(item['sale_item_id'])
            if download_url_id not in download_urls:
                continue

            obj = Item(id=download_url_id,
                       type=item['item_type'],
                       name=item['item_title'],
                       artist=item['band_name'],
                       url=item['item_url'],
                       download_url=download_urls[download_url_id])

            self.items[obj.id] = obj

    @property
    def amount(self):
        """Total number of items in collection according to bandcamp.
        Can be larger than len(items) because of non-downloadable items
        such as subscriptions."""
        return self._amount

    @property
    def items(self):
        """dictionary of sale_id keys to Item namedtuple
         values representing re-downloadable items"""
        return self._items


Item = namedtuple('Item', ('id', 'type', 'name', 'artist',
                           'url', 'download_url'))
