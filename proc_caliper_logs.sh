#! /usr/bin/sh

OUT_FILE=caliper_cluster1.out

grep '| Name' exp_10.out | tail -n 1 > $OUT_FILE
grep '| issueAsset' exp_10.out | tail -n 1 >> $OUT_FILE
grep '| issueAsset' exp_20.out | tail -n 1 >> $OUT_FILE
grep '| issueAsset' exp_40.out | tail -n 1 >> $OUT_FILE
grep '| issueAsset' exp_60.out | tail -n 1 >> $OUT_FILE
grep '| issueAsset' exp_80.out | tail -n 1 >> $OUT_FILE
grep '| issueAsset' exp_100.out | tail -n 1 >> $OUT_FILE
grep '| issueAsset' exp_120.out | tail -n 1 >> $OUT_FILE
grep '| issueAsset' exp_140.out | tail -n 1 >> $OUT_FILE
grep '| issueAsset' exp_160.out | tail -n 1 >> $OUT_FILE
grep '| issueAsset' exp_180.out | tail -n 1 >> $OUT_FILE
grep '| issueAsset' exp_200.out | tail -n 1 >> $OUT_FILE
