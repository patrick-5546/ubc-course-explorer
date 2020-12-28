from django.shortcuts import redirect, render

# search works as a "buffer" for when we are obtaining data
def search(request):
    if request.method == 'GET':
        search = request.GET.get('find')
        # print('search', search)
        return redirect('coursetracker:course', pk=search)

def course(request, pk):
        return render(request, 'coursetracker/course.html')
