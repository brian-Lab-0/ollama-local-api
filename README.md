
# Ollama api from local to api

you can use this to push your local ollama interaction to a rpojetc or even public by adding port forwading to your setup then this will be accable externally

in the given script here example response usage in the screenshot below you can try to call by paasing your question and the result will return from the ollama response line by line small or bigger paragraphs
depending on your answer you can use that case to create responsive text rendering in a much more conversational like in your project


how to use 

```
git clone https://github.com/brian-Lab-0/ollama-local-api.git
```

enter to directory

```
cd ollama-local-api
```


```
pip install langchain_ollama
```

```
python main.py
```

ollama3.1

### type your available model eg run in your terminal ollama list  = ollama3.1

then go to your testing software like postman and use 

```
http://localhost:8089/what is best programming language
```

![Screenshot 2024-12-14 214839](https://github.com/user-attachments/assets/3c6e96b1-6842-4003-baa7-f4bc81b0a2c6)
