# py-fizzbuzz

（Chat-GPTさんが）[Fizz Buzz問題](https://ja.wikipedia.org/wiki/Fizz_Buzz)を解決するコードと、テストコードを作成しました。
Visual Studio Code(以下、VSCode)でテスト実行し、カバレッジを可視化します。
※仕様は、@t_wadaさんこと和田卓人さんの[基調講演の動画](https://www.youtube.com/live/Q-FJ3XmFlT8)から引用させていただきました。

```
# Fizz Buzz問題（仕様）
1から100までの数をプリントするプログラムを書け。
ただし3の倍数のときは数の代わりに「Fizz」と、
5の倍数の時は「Buzz」とプリントし、
3と5両方の倍数の場合には「FizzBuzz」とプリントすること。
```

## 準備

1. pyenv + venvで、Python 3.11.9環境を構築し、poetryを初期化します。

    ```shell
    pyenv install 3.11.9
    pyenv local 3.11.9
    python -m venv venv
    source venv/bin/activate
    poetry init
    ```

1. VSCodeの拡張機能`Coverage Gutters`をインストールし、有効化します。
1. 設定ファイル(.vscode/settings.json)を編集します。venvを使用するため、次の設定が必要です。

    ```json
    {
        "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    }
    ```

## 動作確認1

テストコードをPytestで実行できることを確認します。

1. Python 3.11.9環境の利用を開始します。

    ```shell
    source venv/bin/activate
    poetry install --no-root
    ```

1. テストコードを実行します。

    ```shell
    python -m pytest --cov=apps --cov-report=xml --cov-branch tests/
    ```

1. `coverage.xml`ファイルが生成されます。
1. ソースコード`fizzbuzz.py`を表示します。
1. VSCodeのステータスバーにカバレッジ（網羅率）が表示されていることを確認します。

## 動作確認2

VSCodeの`テスト`でテスト実行します。

1. `テストの実行`ボタンをクリックします。
1. `coverage.xml`ファイルが生成されます。
1. ソースコード`fizzbuzz.py`を表示します。
1. VSCodeのステータスバーにカバレッジ（網羅率）が表示されていることを確認します。
