from main.models import BottomData, ExclusivesData


class ScrapyAppPipeline:

    def process_item(self, item, spider):

        if spider.name == 'bottoms':
            data = BottomData(title=item.get('title'), price=item.get('price'),
                              color=item.get('color'), sizes=item.get('sizes'),
                              description=item.get('description'), specs=item.get('specs'))
            data.save()
            return item

        elif spider.name == 'exclusives':
            data = ExclusivesData(title=item.get('title'), price=item.get('price'))
            data.save()
            return item
        else:
            print('Guess you should check your pipe or a spider')
