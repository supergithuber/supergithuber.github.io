## iOS 打包动态库脚本

此脚本适用于没有引入pod的情况，即没有使用xcworkspace来管理项目，项目中使用的是xcodeproj来管理。

如果项目中使用了pod，需要修改一些--target参数，大体上流程和下诉一致

主要步骤分为：

1. clean缓存
2. 通过xcodebuild打包真机可运行的库，打包模拟器可运行的库
3. 通过lipo合并真机和模拟器的库
4. 打包生成zip，带上podspec
5. 移除打包的中间产物目录，防止下次打包的时候使用上次的中间产物文件，此处有xcodebuild生成的build目录、我自己放二进制压缩包的Library目录

打包脚本示例：

```sh
#!/bin/bash

set -e

echo "[UNQStartTime] buildLoadTImeLibrary start!"

scripts="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "[UNQStartTime] scripts : ${scripts}"


iphonesimulator_sdk="iphonesimulator"
iphoneos_sdk="iphoneos"
targetConfiguration="Release"
targetName="UNQLoadTime"

WRK_DIR="build"
DEVICE_DIR="${scripts}/../${WRK_DIR}/Release-iphoneos/${targetName}.framework"
SIMULATOR_DIR="${scripts}/../${WRK_DIR}/Release-iphonesimulator/${targetName}.framework"

# build for iphoneos
xcodebuild -project "${scripts}/../UNQStartTimeProject.xcodeproj" -target "${targetName}" -configuration "${targetConfiguration}" clean
# build for iphoneos
xcodebuild -project "${scripts}/../UNQStartTimeProject.xcodeproj" -target "${targetName}" -sdk "${iphoneos_sdk}" -configuration "${targetConfiguration}" build
# build for iphone simulator
xcodebuild -project "${scripts}/../UNQStartTimeProject.xcodeproj" -target "${targetName}" -sdk "${iphonesimulator_sdk}" -configuration "${targetConfiguration}" -arch i386 -arch x86_64 build

libraryPath="${scripts}/../Library"
outputPath="${libraryPath}/${targetName}.framework"
if [ -d "${libraryPath}" ]
then
rm -rf "${libraryPath}"
fi

mkdir -p "${outputPath}"

lipo -create "${DEVICE_DIR}/${targetName}" "${SIMULATOR_DIR}/${targetName}" -output "${DEVICE_DIR}/${targetName}"

cp -r "${DEVICE_DIR}/" "${outputPath}/"

if [ -d "${outputPath}/_CodeSignature" ]; then
	rm -r "${outputPath}/_CodeSignature"
fi

#cp dsym file
yes|cp -rf "${DEVICE_DIR}.dSYM" "${outputPath}/../${targetName}-${iphoneos_sdk}.dSYM"
yes|cp -rf "${SIMULATOR_DIR}.dSYM" "${outputPath}/../${targetName}-${iphonesimulator_sdk}.dSYM"

#cp podspec file
yes|cp -f "${scripts}/../UNQLoadTime.podspec" "${outputPath}/../UNQLoadTime.podspec"

echo "[UNQStartTime] buildLoadTImeLibrary finish!"

echo "[UNQStartTime] zip begin"
cd "${libraryPath}"
zip -r -q ${targetName}.zip .
echo "[UNQStartTime] zip end"

```

清除目录脚本示例：

```sh
#!/bin/bash

set -e

# 由buildLoadTimeLibrary负责打包，此脚本负责删除
# 打包目录生成目录 ../Library/UNQLoadTime.zip
# 清除目录 ["../Library", "../build"]

echo "[uploadLoadTimeLibrary] uploadLoadTimeLibrary start!"

scripts="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "[uploadLoadTimeLibrary] scripts : ${scripts}"

# zipName="UNQLoadTime.zip"
# zipPath="../Library/${zipName}"
libraryFolder="../Library"
buildFolder="../build"

# if [ -f "${zipPath}" ]; then
# 	echo "[uploadLoadTimeLibrary] begin upload"
# 	echo "[uploadLoadTimeLibrary] finish upload"
# else
# 	echo "[uploadLoadTimeLibrary] '${zipPath} not exists'"
# fi

if [ -d "${libraryFolder}" ]; then
	rm -rf "${libraryFolder}"
fi

if [ -d "${buildFolder}" ]; then
	rm -rf "${buildFolder}"
fi

echo "[uploadLoadTimeLibrary] uploadLoadTimeLibrary finish!"

```

podspec文件示例：

```ruby
#
#  Be sure to run `pod spec lint UNQStartTimeMonitor.podspec' to ensure this is a
#  valid spec and to remove all comments including this before submitting the spec.
#
#  To learn more about Podspec attributes see http://docs.cocoapods.org/specification.html
#  To see working Podspecs in the CocoaPods repo see https://github.com/CocoaPods/Specs/
#
# 须为静态库
Pod::Spec.new do |s|

  # ―――  Spec Metadata  ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――― #
  #
  #  These will help people to find your library, and whilst it
  #  can feel like a chore to fill in it's definitely to your advantage. The
  #  summary should be tweet-length, and the description more in depth.
  #

  s.name         = "UNQCTime"
  s.version      = "0.2.2"
  s.summary      = "summary"
  s.homepage     = "https://url"
  s.license      = "Copyright"
  s.author       = "sivanwu."
  s.platform     = :ios, "9.0"
  s.source       = { :git => "giturl", :tag => "#{s.version}" }
  s.pod_target_xcconfig = { 'EXCLUDED_ARCHS[sdk=iphonesimulator*]' => 'arm64' }
  s.user_target_xcconfig = { 'EXCLUDED_ARCHS[sdk=iphonesimulator*]' => 'arm64' }

  s.library = 'c++'

  # s.static_framework = true
  
  s.source_files  = ["UNQStartTimeProject/UNQStartTimeMonitor/Classes/CTime/**/*.{h,m,mm,c}", "UNQCTime/UNQCTime.h"]
  s.public_header_files = ["UNQStartTimeProject/UNQStartTimeMonitor/Classes/CTime/UNQCTimeMonitor.h", "UNQCTime/UNQCTime.h"]

end

```

