import Din_massive_in_template_mod, unittest, random, math

def initial_data(Qty=5):
    Values_for_initial_massive=[]
    for i in range(0,Qty):
        Values_for_initial_massive.append(random.randint(0,10**8))
    return Values_for_initial_massive

def data_for_insert(initial_data):
    i=random.randint(0,len(initial_data)-1)
    itm=random.randint(0,10**8)
    data=[]
    data.append(i)
    data.append(itm)
    return data    

def data_for_delete(initial_data):
    i=random.randint(0,len(initial_data)-1)
    data=[]
    data.append(i)
    for j in range(len(initial_data)):
        if i==j:
            data.append(initial_data[i])
            return data

def data_after_delete(initial_data,i):
    new_data=[]
    initial_data_len=len(initial_data)
    for j in range(initial_data_len):
        if j==i:
            for jj in range(j,initial_data_len-1):
                new_data.append(initial_data[jj+1])
            break
        new_data.append(initial_data[j])
    return new_data

def data_after_insert(initial_data,i,itm):
    new_data=[]
    initial_data_len=len(initial_data)
    for j in range(initial_data_len):  
        if j==i:
            new_data.append(itm)
            for jj in range(i+1,initial_data_len+1):
                new_data.append(initial_data[jj-1])
            break
        new_data.append(initial_data[j])
    return new_data  

class Din_massive_tests(unittest.TestCase):

    def test_insert_without_overloading(self):
        #Тест проверяет работу метода вставки элемента при условии отсутствия превышения переполнения буфера
        self.first_dim_massive=Din_massive_in_template_mod.DynArray()
        self.second_dim_massive=Din_massive_in_template_mod.DynArray()
        data_for_first_dim_massive=initial_data()
        data_for_insert_to_first_dim_massive=data_for_insert(data_for_first_dim_massive)
        data_for_second_din_massive=data_after_insert(data_for_first_dim_massive,data_for_insert_to_first_dim_massive[0],data_for_insert_to_first_dim_massive[1])
        for i in range(len(data_for_first_dim_massive)):
            self.first_dim_massive.append(data_for_first_dim_massive[i])
        self.first_dim_massive.insert(data_for_insert_to_first_dim_massive[0],data_for_insert_to_first_dim_massive[1])
        for i in range(len(data_for_second_din_massive)):
            self.second_dim_massive.append(data_for_second_din_massive[i])
        for i in range(len(data_for_second_din_massive)):
            self.assertEqual(self.first_dim_massive[i],self.second_dim_massive[i])
        self.assertEqual(self.first_dim_massive.capacity,self.second_dim_massive.capacity)
        if len(data_for_second_din_massive)>=16:
            len_value=math.ceil(len(data_for_second_din_massive)/16)*16
        else: 
            len_value=16
        self.assertEqual(len_value,self.second_dim_massive.capacity) 

    def test_insert_with_overloading(self):
        #Тест проверяет работу метода вставки элемента в случае необходимости увелечения размера буфера
        self.first_dim_massive=Din_massive_in_template_mod.DynArray()
        self.second_dim_massive=Din_massive_in_template_mod.DynArray()
        data_for_first_dim_massive=initial_data(16)
        data_for_insert_to_first_dim_massive=data_for_insert(data_for_first_dim_massive)
        data_for_second_din_massive=data_after_insert(data_for_first_dim_massive,data_for_insert_to_first_dim_massive[0],data_for_insert_to_first_dim_massive[1])
        for i in range(len(data_for_first_dim_massive)):
            self.first_dim_massive.append(data_for_first_dim_massive[i])
        self.first_dim_massive.insert(data_for_insert_to_first_dim_massive[0],data_for_insert_to_first_dim_massive[1])
        for i in range(len(data_for_second_din_massive)):
            self.second_dim_massive.append(data_for_second_din_massive[i])
        for i in range(len(data_for_second_din_massive)):
            self.assertEqual(self.first_dim_massive[i],self.second_dim_massive[i])
        self.assertEqual(self.first_dim_massive.capacity,self.second_dim_massive.capacity)
        if len(data_for_second_din_massive)>=16:
            len_value=math.ceil(len(data_for_second_din_massive)/16)*16
        else: 
            len_value=16
        self.assertEqual(len_value,self.second_dim_massive.capacity)

    def test_delete_without_shrinking(self):
        #Удаление элемента без изменения размера буфера
        self.first_dim_massive=Din_massive_in_template_mod.DynArray()
        self.second_dim_massive=Din_massive_in_template_mod.DynArray()
        data_for_first_dim_massive=initial_data()
        data_for_delete_in_first_dim_massive=data_for_delete(data_for_first_dim_massive)
        data_for_second_dim_massive=data_after_delete(data_for_first_dim_massive,data_for_delete_in_first_dim_massive[0])
        for i in range(len(data_for_first_dim_massive)):
            self.first_dim_massive.append(data_for_first_dim_massive[i])
        self.first_dim_massive.delete(data_for_delete_in_first_dim_massive[0])
        data_for_second_dim_massive=data_after_delete(data_for_first_dim_massive,data_for_delete_in_first_dim_massive[0])
        for i in range(len(data_for_second_dim_massive)):
            self.second_dim_massive.append(data_for_second_dim_massive[i])
        for i in range(len(data_for_second_dim_massive)):
            self.assertEqual(self.first_dim_massive[i],self.second_dim_massive[i])
        if len(data_for_second_dim_massive)>=16:
            len_value=math.ceil(len(data_for_second_dim_massive)/16)*16
        else: 
            len_value=16
        self.assertEqual(len_value,self.second_dim_massive.capacity)

    def test_delete_with_shrinking(self):
        #Удаление элемента c изменением размера буфера
        self.first_dim_massive=Din_massive_in_template_mod.DynArray()
        self.second_dim_massive=Din_massive_in_template_mod.DynArray()
        data_for_first_dim_massive=initial_data(16)
        data_for_delete_in_first_dim_massive=data_for_delete(data_for_first_dim_massive)
        data_for_second_dim_massive=data_after_delete(data_for_first_dim_massive,data_for_delete_in_first_dim_massive[0])
        for i in range(len(data_for_first_dim_massive)):
            self.first_dim_massive.append(data_for_first_dim_massive[i])
        self.first_dim_massive.delete(data_for_delete_in_first_dim_massive[0])
        data_for_second_dim_massive=data_after_delete(data_for_first_dim_massive,data_for_delete_in_first_dim_massive[0])
        for i in range(len(data_for_second_dim_massive)):
            self.second_dim_massive.append(data_for_second_dim_massive[i])
        for i in range(len(data_for_second_dim_massive)):
            self.assertEqual(self.first_dim_massive[i],self.second_dim_massive[i])
        self.assertEqual(self.first_dim_massive.capacity,self.second_dim_massive.capacity)
        if len(data_for_second_dim_massive)>=16:
            len_value=math.ceil(len(data_for_second_dim_massive)/16)*16
        else: 
            len_value=16
        self.assertEqual(len_value,self.second_dim_massive.capacity)

    def test_exceptions(self):
        #Обработка вставки / удаления элементов из недопустимых позиций
        self.first_dim_massive=Din_massive_in_template_mod.DynArray()
        data_for_first_dim_massive=initial_data()
        itm=1
        j=340
        for i in range(len(data_for_first_dim_massive)):
            self.first_dim_massive.append(data_for_first_dim_massive[i])
        with self.assertRaisesRegex(IndexError, 'Index is out of bounds'):
            self.first_dim_massive.delete(2*self.first_dim_massive.__len__())
        with self.assertRaisesRegex(IndexError, 'Index is out of bounds'):
            self.first_dim_massive.insert(2*self.first_dim_massive.__len__(),itm)

if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()