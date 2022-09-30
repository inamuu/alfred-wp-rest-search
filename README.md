alfred-wp-rest-search
===

## 内容

WordPressの記事データを検索するAlfredのWorkflowです。

## セットアップ

Alfredのsclipt filterがデフォルトで`/usr/bin/python`なので下記でセットアップが必要です。  
`Python 3.9.x` でも動作しますので、`/usr/bin/python3` がある場合は、それをAlfredで指定します。  

次にrequestsライブラリをインストールします。

Python3.9.X

```sh
$ /usr/bin/python3 -m pip install requests
```

Python2.7.X

```sh
$ /usr/bin/python -m pip install requests
```

pip が無い場合

```sh
$ sudo /usr/bin/python -m easy_install pip
```

## 構成
![image](https://user-images.githubusercontent.com/8310973/70435078-406f3500-1ac9-11ea-91e3-e4faf6e7081f.png)

## 検索機能メイン

検索機能は下記のシンプルな構成です。  
![image](https://user-images.githubusercontent.com/8310973/70435121-5846b900-1ac9-11ea-9820-f83e489123b2.png)

### wps(trigger)

このWorkflowの全てと言っても過言ではない根幹の検索部分です。  
直接ファイルを呼び出すことをせずに、Alfredのプログラム呼び出しを使って、書き出しています。  
ちょっと残念なのは `/usr/bin/python` なのでシステムPythonとなり、mojaveだとデフォルト `Python2.7`系なので微妙な点です。  
![image](https://user-images.githubusercontent.com/8310973/70435143-6268b780-1ac9-11ea-901b-168ecbfb9fc9.png)

### openurl

最後に渡された `{query}` をそのまま`DefaultBrowser`で表示させています。  
json形式でないと受け取ることができないので、`wps`の部分でjson形式に変換して渡しています。  
![image](https://user-images.githubusercontent.com/8310973/70435165-72809700-1ac9-11ea-81ec-b130e17988c0.png)

---

## サイトURL登録

ここはノンプログラミングで全て完結しています。
![image](https://user-images.githubusercontent.com/8310973/70435190-83310d00-1ac9-11ea-82d1-3bffd56f3991.png)

### wps_siteurl

まずは引数必須のトリガーを設定します。  
キーワードは`wps`につながる文字がいいので`wps_siteurl`としました。  
![image](https://user-images.githubusercontent.com/8310973/70435195-8b894800-1ac9-11ea-9aa2-a694225f4546.png)

### Write text file

デフォルトのアクションにファイルに書き込むものがあるので、渡ってきた`{query}`をファイルに書き込むようにしています。  
![image](https://user-images.githubusercontent.com/8310973/70435213-980da080-1ac9-11ea-84af-9ecc1cab3a6d.png)

### Post Notification

最後は通知部分です。  
ここはなくても良いのですが、書き込みが完了したことが分かるようにしたかったので追加しました。  
変数を渡すことができるので、表示内容を可変させて通知することができます。  
![image](https://user-images.githubusercontent.com/8310973/70435234-a8258000-1ac9-11ea-9f82-226ae066a4f1.png)
