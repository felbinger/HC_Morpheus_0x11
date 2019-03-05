# Solution of [HC 0x11](https://challenges.the-morpheus.de) from [The Morpheus Tutorials](https://the-morpheus.de)

1. The website contains a field to enter a login token. In the text below the login button is a link to a [development.zip](http://challenges.the-morpheus.de/downloads/development.zip) file.
2. Download and unzip the file, you get a `.class` and a `.jar` file. You can't really do something with the class file, we are going to check if we can decompile the jar file with [JD-GUI](http://jd.benow.ca/).
![IMG](https://i.imgur.com/SP9Drp4.png)
3. Extract the resource (`generateLoginToken`) and the Method (`POST`) from the Client class and try to access it with curl.
```
$ curl -X POST http://185.244.192.170:20018/generateLoginToken
{"expires":"2018-12-25T15:22:06.326503","token":"''E:><rRq[i>EZ_ZYV\\gfUaT~cT+li05,c|z4$,]j2.&wNB-Wl$9.>S$nONX.5o-o8,>1^+O(3XeWR:G&Q5`$X/$V=h-?*ubzJ`Ff'K|%(aAG&fTbN93|M'c)88cEv%A"}
```
4. Ok, lets try to submit this token, hm invalid token. Maybe it's encoded? No in the json data is a expires attribute, lets write a python program to minimize the delay between the token generation and login request.

  ```python
  import requests, bs4

  url = 'http://185.244.192.170:20018'
  flag = ""

  while 'TMT' not in flag:
      token = requests.post(f'{url}/generateLoginToken').json().get('token')
      flag = bs4.BeautifulSoup(requests.post(f'{url}/login', data={'token': token}).text, "html.parser").body.find_all("div", {"class": "alert"})[0].encode_contents().decode()

  print(flag)

  ```

5. Flag: `TMT{y32kTNmdLlBbm4rS1Ysx}`
