#!/bin/sh
set -e

APK_DIR="/var/minis/workspace/abc_kids"
TMP_DIR="/tmp/apk_build"
RM_DIR="/tmp/apk_build_work"

echo "=== Packaging ABC Kids APK ==="

rm -rf "$TMP_DIR" "$RM_DIR"
mkdir -p "$TMP_DIR/assets"
mkdir -p "$TMP_DIR/res/drawable"
mkdir -p "$TMP_DIR/res/mipmap-hdpi"
mkdir -p "$TMP_DIR/META-INF"

# Copy assets
cp "$APK_DIR/index.html" "$TMP_DIR/assets/"

# Minimal AndroidManifest.xml compiled binary or pseudo manifest
cat << 'EOF' > "$TMP_DIR/AndroidManifest.xml"
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.abckids.learnandplay"
    android:versionCode="1"
    android:versionName="1.0">
    <uses-sdk android:minSdkVersion="21" android:targetSdkVersion="33" />
    <application
        android:label="ABC Kids"
        android:hasCode="false">
    </application>
</manifest>
EOF

cd "$TMP_DIR"
zip -r /var/minis/workspace/ABC_Kids_v1.0.apk .

echo "APK packaging finished!"
