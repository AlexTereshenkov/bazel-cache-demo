from python.runfiles import Runfiles

runfiles = Runfiles.Create()

# http_file location
ZSTD_CLI = runfiles.Rlocation("zstd_cli/file/downloaded")

# http_archive location
YQ_CLI = runfiles.Rlocation("yq_cli/yq_linux_amd64")
