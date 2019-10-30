## GribApi.XP

GribApi.XP is a friendly fork of the ECMWF's [GRIB API](https://software.ecmwf.int/wiki/display/GRIB/What+is+GRIB-API). It makes a few changes to improve cross-platform (hence the `XP`) parity of features and packages. At the moment, that mostly means improving support for Windows, but changes for all platforms are welcome.

### GRIB Tools Packages

#### Chocolatey (Windows)

To install the GRIB tools from [Chocolatey](https://chocolatey.org/packages/grib-tools), run
```shell
C:\> choco install grib-tools
```

##### Changes from Vanilla 1.19.0 for Windows
* PNG compression support
* OMP multi-threading enabled by default
* `grib_exit` and `grib_assert` hooks for custom handling of fatal errors (details coming soon)

##### Building
You can build directly with Visual Studio using `./build/Grib.Api.Master.sln`.

To build x86 and x64 libs together, you can run `build\win32\build_gribapi.cmd [re|build] [vs tools version] [Debug|Release] [opt: package version]`, e.g.
```shell
C:\> build\win32\build_gribapi.cmd rebuild 14 Debug
```

### Updating grib_api
Not scripted yet, sorry :(

1. Delete everything in `root/grib_api`.
2. Download the latest version from https://software.ecmwf.int/wiki/display/GRIB/Download
3. **As administrator** (ensures symbolic links are created), extract the files files to `root/grib_api` directory.
4. Commit the vanilla changes to the local repo.
5. Now you need to update the `vcproj` files. This is the tricky bit. There are 2 ways to do this. The second is hacky, but much easier.

##### Method 1 (Hard)
Open a VS Developer Command Prompt.
```shell
> powershell
PS > cd root/grib_api/windows
PS > dir -Recurse *.vcproj | ForEach-Object { devenv /upgrade /q $_.FullName}
```
Copy the preproccors, output directories, etc from the previous GribApi.XP project files to the new ones.
##### Method 2 (Easy)
Do not open the VS Developer Command Prompt. Instead, open the `vcproj` in `grib_api/windows` in a text editor. Copy/paste the list of files from the vcproj files into GribApi.XP's `vcprojx` files.
