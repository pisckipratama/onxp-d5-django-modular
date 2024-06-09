from django.shortcuts import render
from .queries import book_create, book_read, book_read_one_by_id, book_update, book_delete

# Create your views here.

def my_view(request):
    # query = book_create()
    # query = book_read()

    ## Untuk menggunakan dictfetchall
    # for row in query:
    #     print(row['title'])

    # for row in query:
    #     print(row.title, row.author)

    # query = book_read_one_by_id('eb360a79-2272-41e5-b91f-4821f51b21d4')
    # print(query.title, query.author)

    # query = book_update("947f4bde-cdd9-4124-b8f1-1fb45bc8a31c", "Harry Poter", "JK Rowling")
    # print(query)

    query = book_delete("39a5c609-df43-446d-bcdd-5ded3b3e0473")
    print(query)
    name = "Dashboard"
    return render(request, 'app_dashboard/index.html', {'name': name})