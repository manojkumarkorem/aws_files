#item_class
class Item:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        
        #raise_error
        if self.price <= 0:
            raise ValueError('Invalid value for price, got {}'.format(self.price))
        self.category = category
    
    def __str__(self):
        return '{}@{}-{}'.format(self.name, self.price, self.category)

#query_class        
class Query:
    LIST = ['IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
    def __init__(self,field, value, operation = None):
        self.field = field
        self.operation = operation
        if self.operation not in Query.LIST:
            raise ValueError('Invalid value for operation, got {}'.format(self.operation))
        
        self.value = value
    def __str__(self):
        return '{} {} {}'.format(self.field, self.operation, self.value)

#store_class        
class Store:
    #initialization
    def __init__(self):
        self.items = []
        
        
    
    #adding_items
    def add_item(self, new_item):
        self.items.append(new_item)
    
    #printing    
    def __str__(self):
        if self.items == []:
            return 'No items'
        return '\n'.join(map(str,self.items))
    
    #counting_num_of_items_in_the_list
    def count(self):
        return len(self.items)
    
    
    #filtering_items
    def filter(self,query):
        q_obj = Store()
        for item in self.items:
            field_name = query.field
            if query.operation == 'EQ' and getattr(item, field_name) == query.value:
                q_obj.add_item(item)
            elif query.operation == 'GT' and getattr(item, field_name) > query.value:
                q_obj.add_item(item)
            elif query.operation == 'GTE' and getattr(item, field_name) >= query.value:
                q_obj.add_item(item)
            elif query.operation == 'LT' and getattr(item, field_name) < query.value:
                q_obj.add_item(item)
            elif query.operation == 'LTE' and getattr(item, field_name) <= query.value:
                q_obj.add_item(item)
            elif (query.operation == 'STARTS_WITH' or query.operation == 'ENDS_WITH' or query.operation == 'CONTAINS') and query.value in  getattr(item, field_name):
                q_obj.add_item(item)
            elif query.operation == 'IN' and getattr(item, field_name) in query.value:
                q_obj.add_item(item)
        return q_obj
    
    
    def exclude(self, filter_items):
        Temp = Store()
        include_obj = self.filter(filter_items)
        for x in self.items:
            if x not in include_obj.items:
                Temp.add_item(x)
        return Temp