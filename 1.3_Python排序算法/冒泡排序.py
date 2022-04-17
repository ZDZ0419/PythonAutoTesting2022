# 冒泡排序
'''def bubble_sort(arr):
    for i in range(len(arr)-Page):
        for j in range(len(arr)-Page-i):
            if arr[j] > arr[j+Page]:
                arr[j],arr[j+Page] = arr[j+Page],arr[j]
    return arr
list_1=[Page,4,2,6,2,60,34]
print(bubble_sort(list_1))'''
# 冒泡排序
arr =[1,3,2,6,4,5,9,7,0,13]
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort(arr))