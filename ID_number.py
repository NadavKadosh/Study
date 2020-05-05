import string
import functools
class IDIterator():
    def __init__(self, id):
        self._id = int(id)-1
    def __iter__(self):
        return self
    def __next__(self):
        self._id +=1
        if self._id > 999999999:
            raise StopIteration
        while not chek_id_valid(self._id):
            self._id += 1
        return self._id
    def get_len(self):
        return len(str(self._id))

def chek_id_valid(id_number):
    if isinstance(id_number, str):
        is_valid = True
        if not id_number.isnumeric() or id_number.startswith('0') or len(id_number)<9:
            is_valid = False
            return is_valid
        else:
            temp_id = ''
            for i in id_number:
                temp_num = int(i)*2
                if temp_num < 10:
                    temp_id = temp_id+str(temp_num)
                else:
                    temp_num = str(temp_num)
                    temp_num = int(temp_num[0])+int(temp_num[1])
                    temp_id = temp_id + str(temp_num)
            sum_id= functools.reduce(lambda a,b: a+b , [int(i) for i in temp_id])
            if sum_id%10 == 0 and is_valid:
                return True
            else:
                return False
    if isinstance(id_number, int):
        id_number = str(id_number)
        is_valid = True
        if not id_number.isnumeric() or id_number.startswith('0') or len(id_number)<9:
            is_valid = False
            return is_valid
        else:
            temp_id = ''
            for i in id_number:
                temp_num = int(i)*2
                if temp_num < 10:
                    temp_id = temp_id+str(temp_num)
                else:
                    temp_num = str(temp_num)
                    temp_num = int(temp_num[0])+int(temp_num[1])
                    temp_id = temp_id + str(temp_num)
            sum_id= functools.reduce(lambda a,b: a+b , [int(i) for i in temp_id])
            if sum_id%10 == 0 and is_valid:
                return True
            else:
                return False

def id_generator (id_number):
    for i in range (int(id_number), 999999999):
        if chek_id_valid(i):
            yield i
        i += 1

def main():
    my_id = IDIterator(input())
    for i in range(my_id.get_len()):
        print(next(my_id))

    id_gen = id_generator(123456780)
    for i in range (10):
        print (next(id_gen))
if __name__ == '__main__':
    main()