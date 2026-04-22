# 概要

競技プログラミングにおける VSCode の設定ファイルをまとめています。[online-judge-tools](https://github.com/online-judge-tools/oj) と [ac-library](https://github.com/atcoder/ac-library), [kyopro](https://github.com/Chipppppppppp/kyopro) の導入が前提となっています。

# 導入方法

1. 導入していない場合、[online-judge-tools](https://github.com/online-judge-tools/oj) をインストール
2. VSCode 拡張機能に [multi-command](https://marketplace.visualstudio.com/items?itemName=ryuta46.multi-command) をインストール
3. `~/competitive_programming` フォルダを作成
4. フォルダ下に [ac-library](https://github.com/atcoder/ac-library), [kyopro](https://github.com/Chipppppppppp/kyopro) をインストール
5. フォルダ下に `template`, `work` フォルダをダウンロード
6. フォルダ下に `code/main.cpp`, `code/main.py` を作成 (フォルダ、ファイル名は任意)
7. `c_cpp_properties.json` (C/C++ 拡張機能の設定), `keybindings.json` (キーボードショートカット), `cpp.json` (スニペット) の設定をコピペ

# 仕様

- `Alt + N` で新規ファイル作成
- `Alt + Shift + N` で新規フォルダ作成
- `Alt + Enter` で C++/Python のコード実行
- `Alt + Backspace` で C++/Python のコードを `template.cpp`, `template.py` のデフォルト状態に戻す
- VSCode Snippets にダイクストラ法を追加

入出力は `work/input.txt`, `work/output.txt`, `work/error.txt` に表示され、C++ の場合 `work/bundled.cpp` にバンドル結果が表示されるのでこれをコピペして提出します。バンドル時のエラーは `work/bundle_error.txt` に表示されます。
