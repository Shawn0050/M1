# Notebook補足情報

## 動作確認済み環境情報
2022年1月時点で以下の環境で動作確認をしました。

- Anaconda3-2021.11-MacOSX-x86_64
- Google Colaboratory

Google Colaboratoryで利用するための手順に関しては、qiitaに記事 [書籍「ディープラーニングの数学」のNotebookをGoogle Colaboratoryで動かす](https://qiita.com/makaishi2/items/8a7f530ad9b18b1f0b61) を記載しましたので、こちらを参照されて下さい。

2019年4月時点で、Notebookの動作確認は以下の環境で行っています。

- Anaconda 2018.12 for Windows
- Anaconda 2018.12 for Mac
- Watson Studio
- Google Colaboratory


### Windows / MAC

Anaconda3-2021.11-MacOSX-x86_64
ライブラリ別のバージョンは以下の通りとなっています。  
(2022-01時点)

```
python 3.9.7
numpy 1.20.3
pandas 1.3.4
matplotlib 3.4.3
scipy 1.7.1
scikit-learn 0.24.2
jupyter-core 4.8.1

```

### Google Colaboratory
ライブラリ別のバージョンは以下の通りとなっています。  
(2022-01時点)

```
python 3.7.12
numpy 1.19.5
pandas 1.1.5
matplotlib 3.2.2
scipy 1.4.1
scikit-learn 1.0.2
jupyter-core 4.9.1
```


Anaconda 2018.12 for Windows(Mac) Installer  
ライブラリ別のバージョンは以下の通りとなっています。  
(2019-03時点)

```
python 3.7.1
numpy 1.15.4
pandas 0.23.4
matplotlib 3.0.2
scipy 1.1.0
scikit-learn 0.20.1
Jupyter 4.4.0
```

### Watson Studio
ライブラリ別のバージョンは以下の通りとなっています。  
(2019-09時点)

```
python 3.6.8
numpy 1.15.4
pandas 0.24.1
matplotlib 3.0.2
scipy 1.2.0
scikit-learn 0.20.3
Jupyter 4.4.0
```


## 11章のNotebookを動かす方法について
　本書p.309に記載したとおり、Anacondaデフォルト環境にKerasのライブラリは導入されていないため11章付属のサンプルコードは稼働しません（Watson Studio/Google Colaboratoryでは稼働します）。  
　環境構築が難しいため、経験の少ない読者はGoogle Colabの利用をお勧めします。
　また、筆者がMac M1で動作確認したNotebookはch11-keras-mac-m1.ipynbとしてアップしておきましたので、参考とされて下さい。

## Notebookプログラムの制限事項と対応策
2019年3月28日時点で判明しているNotebookプログラムの制限事項と対応策は次の通りです。

|章|プラットフォーム|内容|対策|
|---|---|---|---|
|10|Watson Studio|学習にかなりの時間を要します。|学習自体はできるので結果が戻るまで待っていてください。|

[メインページに戻る](./README.md)