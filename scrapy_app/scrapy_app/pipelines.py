from main.models import BottomData


class ScrapyAppPipeline:

    def process_item(self, item, spider):
        data = BottomData(title=item.get('title'), price=item.get('price'),
                          color=item.get('color'), sizes=item.get('sizes'))
        data.save()
        return item
