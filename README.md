
<div style="width:100px;height:100px; background-color:ffffff;">
<img src="https://github.com/user-attachments/assets/cce1094b-c453-452d-a767-de6dcfcac3cb" alt="Logo" width="50" height="50" >
<img src="https://github.com/user-attachments/assets/5ac333cb-6f7a-4ed6-9457-4f4d02ba015d" alt="Logo" width="70" height="70" >
</div>




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



### type your available model eg run in your terminal ollama list  
example if you have ollama3.1

then type full model name and click enter

then go to your testing software like postman and use 

```
http://localhost:8089/what is best programming language
```

![Screenshot 2025-02-12 030212](https://github.com/user-attachments/assets/160b4d52-e230-4d85-bf15-3f8abff0d15c)




