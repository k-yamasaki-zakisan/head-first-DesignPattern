# OO原則

変化する部分にカプセル化する

継承よりコンポジションを好む

実装に対してではなくインターフェースに対してプログラミングする

相互にやりとりするオブジェクト間には疎結合設計を使用する

クラスは拡張に対しては開かれた状態であるべきであるが、変更に対しては閉じた状態であるべきである

抽象に依存する（具象に依存してはいけない

# command patternまとめ

command-リクエストをオブジェクトとしてカプセル化し、その結果クライアントを異なるリクエスト、キュー、またはログリクエストでパラメータ化でき、undo(前回の実行状態の復元)可能な操作もサポートする


# 重要ポイント

* command patternはリクエストを行うオブジェクトとその実行方法を知っているオブジェクトを分離します

* コマンドオブジェクトがこの分離の中核であり、レシーバの実行でカプセル化します

* マクロコマンドはコマンドの簡単な各拡張であり、複数のコマンドを起動できます。同様に、マクロコマンドはundo(前回の実行状態の復元)を簡単にサポートできます