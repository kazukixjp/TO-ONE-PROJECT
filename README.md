# TO-ONE-PROJECT
時間をかけて調べたリンクが散らばらず一つにまとめられるWEBアプリ・chrome拡張機能「to one」

<h3>システム概要</h3>
他人からの監視されてる感×リンク専門まとめサイト×後で見ようとしていたリンクが散らばらなくなる</br>
「わざわざ保存したリンク＝その人の頭の中」</br>
友人と自分が調べてる途中の資料などを共有できることにより、「程よい他者からの監視されてる感」を実現できます。この感覚が集中力を高めてくれます。それに加えて日頃の膨大な量の検索ページを一つにまとめることができ、「あの時間何してたんだぁ」という感覚の解消につながり、調べごとが好きな人にとってはQOLの向上が期待できます。</br>

<h3>要求</h3>
知識リンク共有特化型SNSです。主な機能は、検索したwebページのリンクを保存できること、それを友人間で共有できること、chrome拡張機能として使えるため即時的にリンクを保存できる。

<理想>
ローカルに自動でリンクが保存されているイメージ（オフライン可）
問題点
MacとWindowsで処理が異なる？？webアプリからローカルディレクトリに保存するアクションができるのか問題


<h3>最低限のアプリ</h3>
Djangoで簡易ユーザ管理システム構築後Herokuへデプロイ

<h3>アイデア</h3>
解析学　「他の人はこの記事を保存しています」というリコメンドシステム

<h3>不安点・メモ</h3>
Webフレームどれ使うべき問題<br>
なぜそのフレームワークを使ったかが大事<br>
絶対聞かれる<br>
将来的にリコメンドシステムを導入するため、pythonはNLPに適してるため<br>
DJANGOでいけそう？？<br>
リンクを保存するアプリは著作権に抵触する？<br>
StudyPlus感のUIが理想<br>
Google chromeとWEB APPはリンクできるのか？<br>
Chromeの拡張機能の方が良い説？？(エッジが効いてて良い)<br>
ディレクトリ構造にすべきか問題<br>
Webアプリ上にディレクトリ構造を作ること＝クラウド？？<br>
Webアプリとローカル環境の連結どうするのか問題浮上<br>
AWS上に置くべき？？<br>
無料の何かがあるか？？？<br>

<h3>動作説明(仕様書)</h3>
検索ページでポップを出し「to one」をクリック後、winndowが出てどのディレクトリに記事を入れるか、名前を変更するか(変更しなければ記事の名前で保存)、

<h3>使用技術</h3>
Python, Django, HTML, CSS, Javascript, Chromeブラウザ

<h3>参考資料</h3>
1.Chrome拡張の作り方 (超概要)
https://qiita.com/RyBB/items/32b2a7b879f21b3edefc

2.kintoneのスレッド投稿がスマートになるChrome拡張をVue.jsで作る
https://qiita.com/RyBB/items/3f343252b0397e93050e

3.Chrome 拡張機能を作ろう前提知識＆ウォーミングアップ編
http://www2.kobe-u.ac.jp/~tnishida/programming/ChromeExtension-01.html

4.Notionリンク
https://seleck.cc/1455

<h3>UI</h3>
デザインアイデア(仮)
<img src="img/to-one-ui-pre" height="400" width="800">

デザインアイデア1
<img src="img/tooneイメージ1.png" height="400" width="800">

デザインアイデア2
<img src="img/tooneイメージ2.png" height="400" width="800">

