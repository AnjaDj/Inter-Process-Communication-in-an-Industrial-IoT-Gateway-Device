# gRPC
## Build and locally install gRPC and Protocol Buffers for C++
1. Configures a directory for locally installed packages and ensures the executables are easily accessible from the command line<br>
    ```bash
     ~$ export LOCAL_INSTALL_DIR=$HOME/.local
     ~$ mkdir -p $LOCAL_INSTALL_DIR
     ~$ export PATH="$LOCAL_INSTALL_DIR/bin:$PATH"
2. Install the basic tools required to build gRPC
     ```bash
     ~$ sudo apt install -y build-essential autoconf libtool pkg-config
3. Clone the grpc repo and its submodules
     ```bash
     ~$ git clone --recurse-submodules -b v1.66.0 --depth 1 --shallow-submodules https://github.com/grpc/grpc
4. Build and locally install gRPC and Protocol Buffers
     ```bash
     ~$ cd grpc
     ~/grpc$ mkdir -p cmake/build
     ~/grpc$ pushd cmake/build
     ~grpc/cmake/build$ cmake -DgRPC_INSTALL=ON \
                              -DgRPC_BUILD_TESTS=OFF \
                              -DCMAKE_INSTALL_PREFIX=$LOCAL_INSTALL_DIR \
                              ../..
     ~grpc/cmake/build$ make -j 4
     ~grpc/cmake/build$ make install
     ~grpc/cmake/build$ popd
     
