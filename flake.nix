{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    devshell = {
      url = "github:numtide/devshell";
      inputs.nixpkgs.follows = "nixpkgs";
      inputs.flake-utils.follows = "flake-utils";
    };
  };

  outputs = { self, nixpkgs, flake-utils, devshell }:
    let flake = system:
      {
        devShells.default = import ./devshell.nix
          (import nixpkgs { inherit system; overlays = [ devshell.overlay ]; });
      };
    in flake-utils.lib.eachDefaultSystem flake;
}
