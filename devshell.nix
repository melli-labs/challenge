nixpkgs:

with nixpkgs;
devshell.mkShell {
  motd = "Hi 👋 and welcome to our hiring challenge!";
  packages = [
    age # Use this to decrypt the `Part-2.md.encrypted`

    # We have added some exemplary languages,
    # you can enable them by uncommenting the respective lines.

    ## C/C++
    # clang

    ## CLOJURE
    # clojure
    # clojure-lsp

    ## GO
    # go

    ## GLEAM
    # gleam

    ## HASKELL
    # ghc
    # haskell-language-server

    ## JAVASCRIPT/ECMASCRIPT OR TYPESCRIPT
    # nodejs
    # deno

    ## PYTHON
    # (python310.withPackages (p: with p; [ numpy ipython black ]))

    ## RUST
    # cargo
    # rustc
    # clippy
    # rust-analyzer
    # rustfmt

    ## ZIG
    # zig
    # zls
  ];

  # Here you can define environment variables
  env = [
    # Uncomment to make rust-analyzer work ;-)
    # {
    #   name = "RUST_SRC_PATH";
    #   value = rustPlatform.rustLibSrc;
    # }
  ];
}
