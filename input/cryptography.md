## 🛡️共通鍵暗号方式

- 暗号化や復号に要する処理時間が <span class="cloze">短い</span> 
-  <span class="cloze">大量のデータ</span> の暗号化・復号に有利。
- 利用者が <span class="cloze">増える</span> と <span class="cloze">通信ごとに異なる共通鍵</span> が必要になり、鍵の数が <span class="cloze">爆発的に増える</span> 
- n人の利用者が相互に通信： <span class="cloze">n(n-1)/2</span> 種類の鍵が必要。
-  <span class="cloze">復号</span> ： 暗号文を平文に戻すこと。
-  <span class="cloze">平文</span> ：暗号化されていないデータ。
-  <span class="cloze">DES </span> ：56ビットの共通鍵を用いるブロック暗号。
-  <span class="cloze">AES </span> ：DESの後継・共通鍵の代表例。
-  <span class="cloze">  RC4  </span> ：SSLやWEPなどで広く使われているストリーム暗号（今は脆弱性のため非推奨）。
-  <span class="cloze">KCipher-2</span> ：九州大学とKDDIが共同開発したストリーム暗号。
- データを固定長の <span class="cloze">ブロック単位</span>で暗号化する方式： <span class="cloze">ブロック暗号</span> 
- データを <span class="cloze">ビット単位</span> あるいは <span class="cloze">バイト単位</span> に逐次暗号化する方式： <span class="cloze">ストリーム暗号</span> 

## 🛡️公開鍵暗号方式

- 暗号化と復号に対となる二つの鍵（ <span class="cloze">鍵ペア</span> ）を利用する方式。
- 鍵ペアは一方の鍵から、 <span class="cloze">もう一方の鍵</span> を推測できない。
- 利用者は、一方の鍵を <span class="cloze">秘密鍵</span> （ <span class="cloze">Private Key</span> ）として他者に知られないよう厳重に管理し、もう一方を <span class="cloze">公開鍵</span> （ <span class="cloze">Public Key</span> ）として公開する。
- 公開鍵方式で暗号通信を行うためには、平文を <span class="cloze">受信者の公開鍵</span> で暗号化する。これを復号できるのは <span class="cloze">受信者</span> のみが持つ <span class="cloze">受信者</span> の <span class="cloze">秘密鍵</span> なので、第三者による  <span class="cloze">盗聴</span> を防ぐことができる。
- 暗号化は <span class="cloze">受信者の公開鍵</span> 、復号は <span class="cloze">受信者の秘密鍵</span> 
-  <span class="cloze">秘密鍵</span> は本人のみが保有し、 <span class="cloze">公開鍵</span> のみ配送することで <span class="cloze">安全な鍵配送</span> が実現。
- n人の利用者が相互に通信： <span class="cloze">2n種類</span> の鍵が必要。
- 不特定多数が同じサイトに送信： <span class="cloze">2種類</span> の鍵が必要。（サイト側が <span class="cloze">受信者</span> 、 <span class="cloze">秘密鍵</span> を持つ・サイト側の <span class="cloze">鍵ペアを使い回せる</span> ）
- 暗号化や復号にかかる処理時間が <span class="cloze">長い</span> 
-  <span class="cloze"> RSA </span> ：大きな数の素因数分解の困難性を利用。
-  <span class="cloze">楕円曲線暗号</span> ：楕円曲線上の離散対数問題が困難であることを利用。
-  <span class="cloze">EIGamal暗号</span> ：位数が大きな群の離散対数問題が困難であることを利用。

## 🛡️セッション鍵方式（ハイブリッド暗号方式）

- 公開鍵方式を使いながらも、暗号化と復号に <span class="cloze">一時的な共通鍵</span> である <span class="cloze">セッション鍵</span> を利用する方式。
- ① 送信者が <span class="cloze">使い捨て</span> の <span class="cloze">共通鍵</span> （ <span class="cloze">セッション鍵</span> ）を生成
- ② 生成した <span class="cloze">セッション鍵</span> を受信者の <span class="cloze">公開鍵</span> で暗号化して送信
- ③ 受信した <span class="cloze">セッション鍵</span> を受信者の <span class="cloze">秘密鍵</span> で復号
- ④ セッション鍵を用いて暗号化通信を行う
- ⑤ 通信が終了したら、双方でセッションを終了する
- 💡鍵のタイプを整理
- 公開鍵暗号（ <span class="cloze">非対称</span> ）
- ・ 暗号化： <span class="cloze">公開鍵</span> （みんなが使える）
- ・ 復号： <span class="cloze">秘密鍵</span> （本人だけが持ってる）
- 共通鍵暗号（ <span class="cloze">対称</span> ）
- ・ 暗号化・復号： <span class="cloze">同じ鍵</span> （＝セッション鍵）
- 💡具体的な流れ
-  <span class="cloze">受信者</span> （例： <span class="cloze">Webサイト</span> ）は 公開鍵・秘密鍵ペアを持ってる。
-  <span class="cloze">送信者</span> （例： <span class="cloze">あなた</span> ）が「使い捨てのセッション鍵」を作る。
-  <span class="cloze">送信者</span> が、そのセッション鍵を受信者の <span class="cloze">公開鍵</span> で暗号化して送信。
-  <span class="cloze">受信者</span> が自分の秘密鍵で復号してセッション鍵を取り出す。
- その後の通信は、**共通鍵暗号（＝セッション鍵）でやりとり**。
- 通信中は暗号化も復号も、**セッション鍵を使う**！

## 💬閑話「でもWebサイト利用してても公開鍵受け取ってる感覚ないなあ」

- 実は、裏ではこっそり・自動で受け取ってる👀
- 🔐 それは「HTTPS」のとき！
- 「https://」って書いてあるサイトにアクセスした瞬間、 裏では
- ① あなたのブラウザ : Webサイトに「HTTPSでアクセスしたいです！」
- ② Webサイト（Webサイトのサーバ）: 証明書（サーバ証明書）を返す。この中に証明情報（発行元、署名など）と **公開鍵** が入ってる🔐
- ③ あなたのブラウザ : 証明書をチェック（改ざんされてない？信頼できる？）
- ④ OKなら、その公開鍵を使って「セッション鍵（共通鍵）」を暗号化して送信する🔐
- 鍵の動作 : **何も知らなくても安全に使えるように**設計されてる。
- 例：公開鍵暗号／証明書／HTTPS通信 ＝ 自動制御
- 攻撃者だったら、**正しくセッション鍵を渡せない／証明書が偽物**
- → だから**その時点で排除される**（通信がブロックされる）
- 💡ログインするときも、買い物するときも、 実はこうなってる。
- ①  その通信が暗号化されているか？（セッション鍵があるか）
- ②  サーバは本物か？（証明書は信頼されているか）
- ③  データは盗まれていないか？改ざんされていないか？
- すべて**コンピュータ（ブラウザとサーバ）が自動で判断**してくれてる。

## 🛡️暗号アルゴリズムの危殆化

- アルゴリズムの安全性は「現実的な時間やコストでは <span class="cloze">解読</span> が不可能である」ことを根拠にしている。
- 暗号解析の進歩やコンピュータの計算能力の向上などにより、暗号アルゴリズムの安全性が低下することを暗号アルゴリズムの <span class="cloze">危殆化</span> とよぶ。
- MD5：衝突（同じハッシュ値を持つ異なるデータ）が簡単に見つかる。
- SHA-1：2017年にGoogleが実際に衝突を発見したことで、実用上の危殆化。
- RSA：鍵長が短い場合 / 現在の性能でも数百bitのRSAは解読可能。
- **安全なアルゴリズムへ移行**する（例：SHA-256やSHA-3への移行）
- **鍵の長さを十分に確保**する（2048bit以上のRSA、256bitのAESなど）

## 💬閑話「人が作るよりずっと安全」完全自動化について

- セッション鍵のランダム生成は完全に自動化されてる。
- プログラムや暗号ライブラリ（例：Python の cryptography モジュール、Javaの KeyGenerator クラスなど）によって
- 安全なランダムな値を使って
- **適切な長さ**（例えばAESなら128bitや256bit）の鍵を
- **高速かつセキュア**に生成する
- セッション鍵の生成は「**安全なランダム**」が超大事🔐
- 普通の random() 関数じゃなくて、 os.urandom() とか、OSレベルの暗号論的乱数生成器（CSPRNG）を使う
- 人間が考えるパスワードや鍵 : けっこう**パターンや癖**がある。
- 人間の直感じゃなくて、**高品質な乱数で機械的に作る**。
- 毎回違う値にする（＝**使い捨てで安全**）
- 長さもきっちりある（128bit以上が推奨）