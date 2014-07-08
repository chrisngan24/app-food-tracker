import entrydao
import db

class Entry:
    def add_entry(self, entry_data): 
        same_entry = entrydao.find_same_entry(entry_data['item_name'], entry_data['date_in'])

        import pdb; pdb.set_trace()
        if same_entry == None:
            print 'hi'
        else:
            import pdb; pdb.set_trace()

