# this should take a list for a receangale
def measurements(a_list):
    def area(a_list):
        #set list_len = length(a_list)
        #len(a_list)
        list_len = len(a_list)
        answer = 0 #define the variable up here
        if list_len == 1:

        # if length is 1: square
            # answer = multiply signle value times iself
            side = a_list[0]
            answer = side*side
        # if length is 2: rectangle
        elif list_len == 2:
            # answer = multiply the values
            side1 = a_list[0] #remember 0 is first item 1-1 = 0
            side2 = a_list[1] #remember second item is 2-1 to get 1
            answer = side1 * side2
        else:
            print('Invalid number of sizes')
            raise ValueError
        # return answer
        return answer
#his is he end of inner function

    def perimeter(a_list):
        #set list_len = lenth(a_list)
        list_len = len(a_list)
        answer = 0
        #define the variable up here
        if list_len == 1:
            answer = a_list[0] * 4
        # if length is 1: square
            # answer = multiply signle value by 4
        # if length is 2: rectangle
        elif list_len == 2:
            # answer = multiply the value 1 by 2 and add to multiply value 2 by 2
        #essentially side 1 + side 2 + side 3 + side4
        # return answer
            answer = a_list[0] * 2 + a_list[1]*2

        else:
            print('Invalid number of sizes')
            raise ValueError

        return answer
    #his is the end of the preimeter function
    # "premiter = {preimeter_output} Area = {acrea_output}"
    # Perimeter = 11.0 Area = 7.14 float output
    area_val = area(a_list)
    pre_val = perimeter(a_list)
    #print (area_val + pre_val)
    return "Perimeter = " + str(pre_val) + "Area = " + str(area_val)

def quick_run(b_list):
    print(measurements(b_list))

if __name__ == '__main__':
#    quick_run([2.1, 2.2])
#    quick_run([2.1])
#    try:
#        quick_run([16, 4, 15])
#    except:
#        print('error occured')
    square = my_local_list = [int(input("Enter a two values for a rectengale"))]

    rectangle = my_local_list = [int(input("Enter a two values for a rectengale")), int(input("Enter a two values for a rectengale"))]
#    my_local_list = [2.1, 3.4]
    print(measurements(my_local_list))


