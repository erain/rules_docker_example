package(default_visibility = ["//visibility:public"])

licenses(["notice"])  # Apache 2.0

load("@examples_grpc//:requirements.bzl", "requirement")
load("@io_bazel_rules_docker//python:image.bzl", "py_image")

py_binary(
    name = "server_binary",
    srcs = [
        "server.py",
    ],
    main = "server.py",
    deps = [
        requirement("grpcio"),
        "//hello_grpc/proto:py",
    ],
)

py_image(
    name = "server",
    srcs = [
        "server.py",
    ],
    base = "@py_debug_image_base//image",
    deps = [
        requirement("grpcio"),
        requirement("setuptools"),
        "//hello_grpc/proto:py",
    ],
)
