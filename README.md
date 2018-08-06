Django-GraphQL-chat_project
=============

This project demonstrates the construction of API using graphQL technology. An example shows how to create a chat for two users.

## Installation ##

In order to work on your own version of the this project, please **fork this repository**.

How to run this project locally
=============================

1.Create and activate environment

2.Install dependencies from requirements.txt file.

3.Navigate to the projects root directory and run project with `python manage.py runserver` command.



Test queries and mutation
=============================

API is available at 127.0.0.1:8000/graphql root.

Here is available to create chat messages. 

```mutation{
  createMessage(
    userId:1
    text: "New message"
  ) {
    message {
      text
    }
  }
}
```

Message text is required argument. ```userId``` shoul be provided if not ```dialogId```


Get all messages from the same chat

```query{
  dialog(id:$dialogId){
    user1{
      id
      username
    }
    user2{
      id
      username
    }
    message{
      id
      text
    }
  }
}
```


Only registered users have access to api. There are two auxiliary URLs:
``` 127.0.0.1:8000/signup ``` - for registration
``` 127.0.0.1:8000/login ``` - for authorization
