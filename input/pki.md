## 🔒PKI 公開鍵基盤

- 公開鍵基盤：Public Key Infrastructure 
- **PKI** ：**暗号技術** を「 <span class="cloze">信頼できる形</span> 」で**社会に提供**するための仕組み。
- 別々に存在している技術（暗号）（認証）→ 現実インフラとして安全に使えるようにする。
-  <span class="cloze"> PKI </span>  =  **提供・管理・運用する「仕組み」** 
- ・ 公開鍵とその所有者を対応付けるための基盤
- **信頼のネットワーク**：個人、企業、政府、ソフトウェア会社、すべての <span class="cloze">合意</span> と <span class="cloze">協力</span> で成り立つ。
- 💡**1つの会社でPKI**は <span class="cloze">構築</span> できず、 <span class="cloze">信用</span> もされない。
- 🏛️ **PKIに必要な 代表的な5つの組織分類**：
- ① ユーザー企業：証明書を使う（Webサーバ、メールなど）
- ② 認証局（CA）：証明書を発行・管理
- ③ 登録局（RA）：本人確認（CAの代理）
- ④ ソフトウェア提供者：ブラウザ、OSなどに「 <span class="cloze">信頼できるCAリスト</span> 」を持ってる
- ⑤ ブラウザ/OSベンダー： <span class="cloze">ルート証明書</span> を信頼する（例：Microsoft, Apple, Mozilla）
- 💡PKIにおける工程と役割
<table>
  <tr>
	<th >工程</th><th>内容</th><th>誰が実施？</th><th>PKIの中の役割</th>
  </tr>
  <tr>
    <td>証明書の発行</td><td >利用者の公開鍵をCAが証明書にする</td><td>CA（認証局）</td><td >信頼できる第三者として</td>
  </tr>
  <tr>
    <td>証明書の配布</td><td >CAから利用者やサーバーへ証明書を送付する</td><td>CA（認証局）</td><td >証明書の流通・管理</td>
  </tr>
  <tr>
    <td>証明書の提示</td><td >通信時に相手に自分の証明書を提示する</td><td>利用者やWebサーバなど</td><td >通信相手に自分の証明書を提示</td>
  </tr>
  <tr>
	  <td>証明書の検証</td><td >CAの署名が正しいか？有効期限は失効してないか？</td><td>通信相手・クライアント</td><td >相手が本物か確認する</td>
  </tr>
  <tr>
	  <td>信頼チェーンの確認</td><td >そのCAを信頼できるか？ルートCAまでたどれる？</td><td>ブラウザやOSに内蔵された信頼リスト</td><td >PKIの「信頼の連鎖」構築</td>
  </tr>
</table>

## 🏛️認証局 CA : Certificate Authority

- 🔑公開鍵が正しく本人のものであることは、信頼できる第三者が保証する必要がある。
- **信頼できる第三者機関** =  <span class="cloze">認証局（CA）</span> 
- 認証局：本人情報を確認の上、本人の <span class="cloze">公開鍵</span> に保証を与えた証明書「 <span class="cloze">デジタル証明書</span> 」を発行
- 利用者：証明書から「認証局が認めた公開鍵」を取得し、安全な通信に利用する

## 📜デジタル証明書

-  <span class="cloze">X.509</span> ：ITU-T が定めた証明書の規格
- 🧾 証明書の本体（署名前）
<table>
  <tr>
	<th>フィールド名</th><th>説明</th>
  </tr>
  <tr>
    <td>バージョン</td><td >証明書のバージョン情報</td>
  </tr>
  <tr>
    <td>シリアル番号</td><td >証明書を一意に識別する番号</td>
  </tr>
  <tr>
	  <td>認証局の識別名</td><td >証明書を発行したCAの識別名</td>
  </tr>
  <tr>
	  <td>有効期限</td><td >証明書の有効期間（開始日〜終了日）</td>
  </tr>
  <tr>
	  <td>公開鍵所有者の識別名</td><td >証明書の利用者の識別名</td>
  </tr>
  <tr>
	  <td>公開鍵</td><td >利用者の公開鍵</td>
  </tr>
  <tr>
	  <td>証明書の署名アルゴリズム</td><td >認証局が使った署名方式（例：SHA256withRSA）</td>
  </tr>
</table>
- ✍️ 認証局が上記に署名（メッセージダイジェスト＋秘密鍵で暗号化）
- 📜完成したX.509証明書（署名付き）
<table>
  <tr>
	<th>フィールド名</th><th>説明</th>
  </tr>
  <tr>
    <td>バージョン</td><td >証明書のバージョン情報</td>
  </tr>
  <tr>
    <td>シリアル番号</td><td >証明書を一意に識別する番号</td>
  </tr>
  <tr>
	  <td>認証局の識別名</td><td >証明書を発行したCAの識別名</td>
  </tr>
  <tr>
	  <td>有効期限</td><td >証明書を発行したCAの識別名</td>
  </tr>
  <tr>
	  <td>公開鍵所有者の識別名</td><td >証明書の利用者の識別名</td>
  </tr>
  <tr>
	  <td>公開鍵</td><td >利用者の公開鍵</td>
  </tr>
  <tr>
	  <td>証明書の署名アルゴリズム</td><td >認証局が使った署名方式（例：SHA256withRSA）</td>
  </tr>
  <tr>
	  <td>認証局のデジタル署名</td><th>← ここに追加された</th>
  </tr>
</table>
- 認証局のデジタル署名が確認できれば、公開鍵は「証明書に記載された本人所有のもの」

## 📄失効リスト CRL：Certificate Revocation List

- 公開鍵の漏洩や誤発信など、何らかの理由によって有効期限内に証明書が失効したもののリスト。
- ・認証局から定期的に配布される
- 💡署名や有効期限だけでなく、 **証明書がCRLに含まれていないかどうか** も確かめよう！
- 🧩 CRLの基本構成（X.509 CRL）
<table>
  <tr>
	<th>フィールド名</th><th>説明</th>
  </tr>
  <tr>
    <td>バージョン</td><td >CRLのバージョン（現在はv2が主流）</td>
  </tr>
  <tr>
    <td>発行者識別名</td><td >このCRLを発行した認証局（CA）の識別名</td>
  </tr>
  <tr>
	  <td>発行日時</td><td >CRLを発行した日時</td>
  </tr>
  <tr>
	  <td>次回更新日時</td><td >次のCRLが発行される予定の日時</td>
  </tr>
  <tr>
	  <td>失効リスト</td><td >失効した証明書の一覧（それぞれに「シリアル番号」「失効日時」などが含まれる）</td>
  </tr>
  <tr>
	  <td>署名アルゴリズム</td><td >このCRLに署名する際に使ったアルゴリズム</td>
  </tr>
  <tr>
	  <td>CAのデジタル署名</td><td >CRLの本体をCAがハッシュ→秘密鍵で署名したもの（改ざん防止）</td>
  </tr>
</table>
- 🧭 CRLの流れ
- ① CAが失効すべき証明書の情報を収集
- ② CRLの本体を作る（失効リスト含む）
- ③ 本体にハッシュをかけて、CAの秘密鍵で署名
- ④ 完成したCRLを公開（証明書検証時に使われる）

## 🕓OCSP：Online Certificate Status Protocol

- デジタル証明書が有効かどうかを認証局に問い合わせるプロトコル。
- 失効状態を <span class="cloze">オンライン</span> で <span class="cloze">リアルタイム</span> に確認する。
- CRL方式に比べ、失効状態を <span class="cloze">よりタイムリー</span>に確認できる 。
- 必要な証明書だけ確認するから <span class="cloze">軽量</span> 

## 💡PKIによる認証＆ 認証局の階層

- 認証局の階層：**信頼の連鎖** をつくる仕組み（ルートCA → 中間CA → 利用者証明書）
- 🔗「そのCAを信頼できるのか？」という疑問を解消する仕組み
- ① クライアントが証明書を受け取る。
- ② 証明書の署名（デジタル署名）を検証するために、**その署名をしたCAの証明書（公開鍵）を使う**。
- ③ でも、「 **そのCAが本物か？** 」をさらに検証したい（さらに上位のCAへ…）
- ④最終的に**ルートCA**までたどり着ければ「信頼の連鎖」が成立。
- 🏛️**CAの階層構造** ：最終的に「ルートCAまで信頼の連鎖がつながればOK！」
- ・ ルートCAは、ブラウザやOSが最初から信頼してる
- ・ だから、ルートからの署名の連鎖で「信頼できる証明書だ」と判断できる
- 💡なんでルートCAだけじゃないの？
- ・ ルートCAは「**絶対的な信頼の源**」：ルートCAの秘密鍵が漏れたり不正利用されたら世界中の信頼関係が崩壊！
- 🛡️ 中間CAを使うメリット
<table>
  <tr>
	<th>メリット</th><th>内容</th>
  </tr>
  <tr>
    <td>セキュリティの分離</td><td >ルートCAはオフラインにして保管 → 滅多に使わない</td>
  </tr>
  <tr>
    <td>柔軟な運用</td><td >中間CAを複数用意して、用途や会社ごとに分担できる</td>
  </tr>
  <tr>
	  <td>インシデント対応</td><td >中間CAに問題があっても、ルートは無事 → すぐ入れ替え可能</td>
  </tr>
</table>
- 証明書を発行したCAを信頼していないとき、自分が信頼するCAまで認証チェーンを遡る。
- ルート証明書：認証局が自身の正当性を証明するために、自ら署名したもの。

## 🧱ルート証明書

- PKIにおける最上位の証明書：
- 一番上にいる「ルート認証局（Root CA）」が自ら発行し、自ら署名している（＝ <span class="cloze">自己署名証明書</span> ）
- このルート証明書が**信頼の起点**（ <span class="cloze">トラストアンカー</span> ） となる。
- すべての証明書の信頼は、最終的にルート証明書までたどって確認する。
- ルート証明書が信頼されているからこそ、その下位（中間CAや利用者証明書）も信頼できると判断される。
- 🔁「**自分で自分を証明**」ってどういうこと？
- 😎 「私はルートCAです（自分で名乗る）」
- 😎 「その証明は…私がしました（自己署名）」
-  **他人の証明に頼らない唯一の証明書**
- なぜ信頼できるの？：**OSやブラウザが「信頼してもいい」と決めてる** から！
- PCやスマホの中には「このルート証明書は信頼してOK！」というリストが入ってる。
- ルート証明書は「**誰かに証明されているわけじゃないのに、みんなが“この人は信用できる”と前提にしてる先生みたいな存在**」
- 🔒信頼の構造（ITと現実の対比）※AI出力
<table>
  <tr>
	<th>ITの世界の「信頼」</th><th>現実世界の「信頼」</th>
  </tr>
  <tr>
    <td>OSやブラウザに内蔵されたルート証明書</td><td >国や公共機関が「この身分証は正当です」と認めている</td>
  </tr>
  <tr>
    <td>ルートCA（自己署名）</td><td >国家が発行するパスポート</td>
  </tr>
  <tr>
	  <td>中間CA → サーバー証明書</td><td >市役所で発行された住民票</td>
  </tr>
</table>
- AppleやMicrosoftが“民間の国”として「この人たちは本物です」と言ってるような構図
- 信頼を管理するための基準：
- ・ Apple, Microsoft, Mozillaなどには「**ルートプログラム**」という参加基準がある（運営実績・セキュリティ対策・監査レポート提出など）
- ・ 国が発行する電子証明書（JPKIなど）も、一部ルート証明書として使われる
- ・ アメリカやEUでは、ある種の「準公的な認証局（Federal PKI）」も存在する

## 🔗 誰が誰を保証してるの？

- インターネットのTLS証明書
<table>
  <tr>
	<td>Apple / Microsoft / Mozilla（ブラウザやOS提供者）</td>
  </tr>
  <tr>
    <th>↓ 信頼してる</th>
  </tr>
  <tr>
    <td>ルートCA（自己署名、民間企業）</td>
  </tr>
  <tr>
	  <th> ↓ 証明してる</th>
  </tr>
    <tr>
	<td>中間CA（大手CAの子会社とか）</td>
  </tr>
  <tr>
    <th> ↓ 証明してる</th>
  </tr>
  <tr>
    <td>Webサイトの証明書（httpsの証明書）</td>
  </tr>
  <tr>
	  <th> ↓ 証明してる</th>
  </tr>
   <tr>
    <td>ユーザー（「あ、このサイト安全だな」）</td>
  </tr>
</table>
- 信頼の起点は、「**OSやブラウザに内蔵されてるルート証明書**」
- → **中央集権的**な「信頼モデル」（TLS, CA）
- 🌐分散型で「**信頼できるルールで全員が合意形成してる**」のが、ブロックチェーン
- ✅ TLS（ルート証明書）：中央集権的な「信頼モデル」
- ・ 信頼の出発点は「OSやブラウザが内蔵してるルート証明書」
- ・ 誰か（AppleやMicrosoftなど）が「これは信頼できるよ」と**お墨付き**を出している。
- ・証明書は **階層的（ピラミッド構造）** になっていて、信頼の連鎖がある。
- ✅ ブロックチェーン：分散型の「信頼モデル」
- ・ 誰も「この人が正しい」と決めない。
- ・ 改ざんが起きにくく、**全体の合意が信頼のベース**。
- どちらも「証明」がカギ
<table>
  <tr>
	<th>観点</th><th>TLS（ルート証明書）</th><th>ブロックチェーン</th>
  </tr>
  <tr>
    <td>誰が証明？</td><td >認証局（CA）とブラウザ/OS</td><td >全ノード（分散合意）</td>
  </tr>
  <tr>
    <td>信頼の仕組み</td><td >信頼された第三者が階層的に証明</td><td >自律的なルールと検証で合意</td>
  </tr>
  <tr>
	  <td>セキュリティの方向性</td><td >「誰が署名したか」をチェック</td><td >「改ざんできない記録」をチェック</td>
  </tr>
</table>
- 「**誰が誰を信頼するか／しないか**」「**中央 vs 分散**」「**権威 vs 合意**」ITの世界でずっと問われてる哲学🤔

## 🌎 信頼のしくみ：中央集権 vs 分散

- ルート証明書から広がる「信頼と権力の構造」
- ・一番上（ルート）の証明書は「 <span class="cloze">自己署名（自分で自分を保証）</span>」している。
- ・OSやブラウザに「この人は信頼していいよ」とあらかじめ登録されている。
- → 「公的機関がこの先生を信頼してるから**私たちも従う**」状態。
- 🔗 2000年代、Winny登場、スノーデンの告発で揺れ動く信頼の仕組み
<table>
  <tr>
	<th>中央集権型</th><th>分散型</th>
  </tr>
  <tr>
    <td>権威ある一箇所が保証</td><td >複数の人・ノードが相互に検証</td>
  </tr>
  <tr>
    <td>信頼は「上から」くる</td><td >信頼は「ネットワークで合意」される</td>
  </tr>
  <tr>
	  <td>国・大企業・CA（認証局）</td><td >ブロックチェーン・ピア同士の署名</td>
  </tr>
</table>
- 💡キーワード「ピア（peer）＝対等な相手」
- 🌐  <span class="cloze">クライアント・サーバー</span> **方式**（中央集権型）
- 例：YouTube
- 　→ YouTubeのサーバーに動画がある
- 　→ 視聴者はそこにアクセスして見るだけ
- 🔁  <span class="cloze">ピア・ツー・ピア</span> （P2P・分散型）
- 例：Napster、Winny、BitTorrent
- 　→ ユーザー同士が <span class="cloze">自分の持ってるファイルの一部</span> を出し合う
- 　→ 誰か1人がサーバーってわけじゃない
- 　→ みんなが「ピア（＝仲間・対等な相手）」として動いてる
- 💡**インターネットの最初の設計思想は分散型**！
- ① 初期構想（ARPANET）は、核攻撃などで <span class="cloze">一部が破壊されても機能し続ける</span>ための分散型ネットワークとして設計されていた。
- ② Webの商業化とともに、 <span class="cloze">大規模サーバー</span> を持つプラットフォームが主流（Yahoo!、Googleなど）
- ③ P2Pの概念が一般に広まり、分散型への回帰の兆し（ナップスターなど）
- ④  <span class="cloze">クラウドコンピューティング</span> の台頭で再び中央集権的なモデルへ（Google, Apple, Facebook, Amazonが「GAFA」と呼ばれ象徴的になった）
- ⑤  <span class="cloze">ブロックチェーン</span> 技術の台頭で再び分散型への関心

## 🌎 影響のあった出来事 / Napster vs Metallica 

- メタリカの**未発表曲「I Disappear」** が Napster で**流出＆拡散**
- → Napsterを訴える！（2000年4月）
- ⚖️ 訴訟のポイント：
- ・Napster ：中央サーバーでは保存してない、**ユーザー同士のやりとり** を主張
- ・メタリカ：「**著作権侵害**を助けてる」と猛反発
- ・ナップスター上で流通した音楽データの多くは著作権を無視した市販のCDなどからの違法コピー
- ・2001年7月に、メタリカとナップスターが双方歩み寄る形で決着（詳細は公表されず）
- 🔄 Napster → Spotify の系譜
<table>
  <tr>
	<th >時代</th><th>サービス</th><th>Point1</th><th>Point2</th>
  </tr>
  <tr>
    <td>1999年頃</td><td >Napster</td><td>P2Pで音楽ファイル（MP3）をユーザー同士が共有</td><td >違法DLの温床にも → 訴訟 </td>
  </tr>
  <tr>
    <td>2000年代</td><td >Kazaa, LimeWire など</td><td>Napsterの後継的なP2P型ファイル共有ソフト</td><td >著作権の問題を無視したサービスが乱立</td>
  </tr>
  <tr>
    <td>2003年〜</td><td >iTunes Store</td><td>音楽を「購入」してDLする合法なサービス</td><td >アップルが音楽業界に秩序を戻す</td>
  </tr>
  <tr>
	  <td>2008年〜</td><td >Spotify</td><td>音楽は“所有”から“ストリーミング”へ</td><td >月額で聴き放題、正当な権利処理、合法的</td>
  </tr>
</table>
- 💡 ナップスターを共同創設したショーン・パーカー（Sean Parker）はのちにFacebookの初期投資家となり、同社の初代社長に就任。
- 🎧 **Spotify は分散型？**
<table>
  <tr>
	<th >項目</th><th>Napster</th><th>Spotify</th><th>YouTube</th>
  </tr>
  <tr>
    <td>仕組み</td><td >P2P（分散）</td><td>クライアント・サーバー（中央集権）</td><td >クライアント・サーバー（中央集権）</td>
  </tr>
  <tr>
    <td>配信者</td><td >ユーザー全員が提供者（勝手に共有）</td><td>提携した音楽提供者（レーベル等）</td><td >誰でも配信可能（審査はある）</td>
  </tr>
  <tr>
    <td>手続き</td><td >勝手にファイル共有（著作権なし）</td><td>正規契約の上で曲を公開</td><td >利用規約に基づいて動画公開（審査後）</td>
  </tr>
  <tr>
	  <td>著作権</td><td >無視されがちだった（違法）</td><td>完全合法（ライセンス契約済）</td><td >条件付き合法（削除されることも）</td>
  </tr>
   <tr>
	  <td>管理者</td><td >実質的にはいなかった</td><td>Spotify社</td><td >Google社（YouTube）</td>
  </tr>
</table>
- 🔄 仕組みは分散じゃなくても「自由な発信・共有」の思想はSpotifyやYouTubeで実現された。
- ✅ Spotify、初期はP2Pとのハイブリッドだった。

## 🌎 影響のあった出来事 / Winny（ウィニー）

- **Winny**：2002年に金子勇氏によって開発・公開されたファイル共有ソフト。
- **特徴**：P2P型、**匿名性が高く、中央サーバを介さない**設計（分散型）。
- 🕓 時系列
<table>
  <tr>
	<th>年</th><th>出来事</th><th>反応など</th><th>世界</th>
  </tr>
  <tr>
    <td>2002</td><td >Winny公開</td><td>新技術として注目される</td><td ></td>
  </tr>
  <tr>
    <td>2003</td><td >ウイルス事件等で注目</td><td>セキュリティリスク拡大、報道過熱</td><td ></td>
  </tr>
  <tr>
	  <td>2004</td><td >金子勇氏逮捕</td><td>技術者の逮捕が波紋を呼ぶ</td><td >P2P技術ベースのSkype正式リリース</td>
  </tr>
  <tr>
    <td>2006</td><td >第一審：有罪判決</td><td>技術者の署名運動はじまる</td><td >Google が YouTube を傘下に</td>
  </tr>
   <tr>
	  <td>2007</td><td ></td><td></td><td >初代iPhone発売<br>Netflixがストリーミング配信に移行</td>
  </tr>
   <tr>
	   <td>2008</td><td ></td><td></td><td >P2P利用の音楽配信Spotifyスタート<br>初期はクライアントサーバ型＋P2P型のハイブリッド</td>
  </tr>
  <tr>
    <td>2009</td><td >二審で逆転無罪</td><td>議論深まる</td><td ></td>
  </tr>
  <tr>
	  <td>2011</td><td >最高裁で 無罪確定</td><td>正式に無罪、再評価の始まり</td><td ></td>
  </tr>
  <tr>
	  <td>2012</td><td >情報処理学会などで再評価の声</td><td>「技術はどう評価すべきか」が問われ始める</td><td ></td>
  </tr>
  <tr>
    <td>2013</td><td >金子勇氏、心筋梗塞で永眠（享年42）</td><td></td><td ></td>
  </tr>
  <tr>
    <td>2014</td><td ></td><td></td><td >Spotify：モバイル通信時代に入り、端末間通信（P2P）から完全なクライアントサーバ型に移行</td>
  </tr>
  <tr>
    <td>2018</td><td >情報処理学会から顕彰</td><td>社会的な名誉回復へ</td><td ></td>
  </tr>
</table>
- **Winnyの何がすごかったのか？**
- ・P2P技術を、当時の日本で高性能に実装。
- ・サーバーを介さずに、匿名性を高く保った設計。（←今でいう分散型の思想）
- ・それまでの他の分散型は「サーバーを減らすこと」が目的だった。
- **プログラムとしての難しさ**
- ・ネットワーク・暗号・分散処理の知識が全部必要。
- ・C++での実装で、低レイヤーの工夫が凝らされていた。
- **Winny開発の動機** 
- → 「ファイル交換ソフトは海外にもいろいろあるけど、日本発で新しいものができないか、技術的興味から取り組んだ」
- **情報処理学会**が彼の**功績を顕彰**した際に使った言葉：
- → 「新たなP2Pネットワークの可能性を切り拓いた先駆的功績は、今なお情報技術の進歩に大きな示唆を与える」
- 🔗 Point
-  <span class="cloze">P2P通信</span> ：ピア（利用者）同士が直接データをやりとりする通信方式。中央サーバを介さない。
-  <span class="cloze">分散処理</span> ：処理を複数ノードで分担。Winnyはその一例。
-  <span class="cloze">匿名性</span> ：ノードの身元を秘匿する。Winnyの特徴でもあり、問題視もされた。
-  <span class="cloze">情報漏洩</span> 対策：Winny経由で機密情報流出が多発し、セキュリティ教育・対策の必要性が顕在化。
- 組織の <span class="cloze">セキュリティポリシー</span> ：ファイル共有ソフトの利用制限など、内部規定の重要性が再認識された。
-  <span class="cloze">著作権法</span> とIT：技術提供者が違法利用者を幇助したとされ逮捕された例。技術と法の関係の事例として重要。
-  <span class="cloze">幇助罪</span> ：他人の違法行為を手助けしたとされる場合の刑事責任。
- **技術の中立性**：技術そのものは中立であり、使い方の問題という観点。
- **技術者倫理**：開発者がどこまで利用者の行動に責任を持つべきか。





