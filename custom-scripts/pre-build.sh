#!/bin/sh

cp $BASE_DIR/../custom-scripts/S41network-config $BASE_DIR/target/etc/init.d
cp $BASE_DIR/../custom-scripts/S50srv $BASE_DIR/target/etc/init.d
chmod +x $BASE_DIR/target/etc/init.d/S41network-config
chmod +x $BASE_DIR/target/etc/init.d/S50srv
