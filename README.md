# 概要

競技プログラミングにおける VSCode の設定ファイルをまとめています。[online-judge-tools](https://github.com/online-judge-tools/oj) と [ac-library](https://github.com/atcoder/ac-library), [kyopro](https://github.com/Chipppppppppp/kyopro) の導入が前提となっています。

# 導入方法

1. [online-judge-tools](https://github.com/online-judge-tools/oj) をインストール
2. VSCode 拡張機能に [multi-command](https://marketplace.visualstudio.com/items?itemName=ryuta46.multi-command) をインストール
3. `competitive_programming` フォルダを作成、以下これをワークスペースとする (フォルダ名は任意)
5. ワークスペース下に [ac-library](https://github.com/atcoder/ac-library), [kyopro](https://github.com/Chipppppppppp/kyopro) をインストール
6. ワークスペース下に `template` フォルダをダウンロード
7. ワークスペース下に `work` フォルダを作成
8. ワークスペース下に `code` フォルダを作成し、`code/main.cpp`, `code/main.py` の二つのファイルを作成 (フォルダ名、ファイル名は任意)
9. `.vscode/c_cpp_properties.json` (C/C++ 拡張機能の設定), `.vscode/settings.json` (ワークスペースの設定), `keybindings.json` (キーボードショートカット), `cpp.json` (スニペット) の内容をコピペ
10. ワークスペースを VSCode で開き、分割してファイルを表示するなどして環境を整える

# 仕様

- `Alt + N` で新規ファイル作成
- `Alt + Shift + N` で新規フォルダ作成
- `Alt + Enter` で C++/Python のコード実行
- `Alt + Backspace` で C++/Python のコードを `template.cpp`, `template.py` のデフォルト状態に戻す
- VSCode Snippets にダイクストラ法を追加

入出力は `work/input.txt`, `work/output.txt`, `work/error.txt` に表示されます。

C++ の場合、コンパイルエラーの時は `work/output.txt` にエラー内容が表示されるようになっています。`work/compile_error.txt` でコンパイル時の警告を確認することもできます。提出時はバンドル済みの `work/bundled.cpp` をコピペして使用します。バンドル時のエラーは `work/bundle_error.txt` に表示されます。

コード、バンドル結果、入力、出力を以下のように分割して表示すると便利です。

<img width="1920" height="1032" alt="image" src="https://github.com/user-attachments/assets/b15afcdf-715f-4a84-831b-ae5fc3ee6fbc" />

また、以下を実行することで `all.hpp.gch` を作成しコンパイル時間を短縮するのもよいでしょう。

```bash
g++ -std=gnu++23 -O2 -Wall -Wextra -mtune=native -march=native -Iac-library -Ikyopro kyopro/kpr/all.hpp
```

# 備忘録 - おすすめ VSCode 拡張機能

- [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme): ファイルアイコン
- [indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow): インデントのカラーリング
- [Trailing Spaces](https://marketplace.visualstudio.com/items?itemName=shardulm94.trailing-spaces): 不要なスペースを可視化
