from django.shortcuts import render
from django.contrib import messages


# Create your views here.
def message(request):
    # if 'my_message_displayed' not in request.session:
    #     messages.success(request, 'This message will be deleted after it is first displayed.')
    #     request.session['my_message_displayed'] = True
    # else:
    #     # message has already been displayed, so delete it
    #     message_object = messages.get_messages(request)
    #     print(message_object)
    #     if message_object:
    #         for message1 in message_object:
    #             message1.delete()
    # message_object.delete()

    # message_object = messages.get_messages(request)
    # print(message_object)
    # if message_object:
    #     for message1 in message_object:
    #         message1['request'].delete()
    #         # print(message1['request'].delete())
    #         del message1
    if request.method == 'POST':
        # print(request.POST)

        messages.error(request, request.POST['message'])

    return render(request, 'message.html')
