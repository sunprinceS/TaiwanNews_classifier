New or Old ? Who are you?
===
## 新舊媒體分類器
* More Info : 請參閱繳交的html檔

## 如何執行
* Prerequisities:
	* ipython2
	* python-setuptool
	* R(jiebaR,tmcn,tm)
	* python>=2.7.10(scikit-learn,numpy,matplotlib)

* 到release下載model檔
	* 將 SPEECH.\* 放到 src/libsvm/python/transformModel下
	
* 打開terminal，執行```ipython2 notebook```，如果成功會看到以下訊息
![](http://i.imgur.com/Eu7N2vv.png)

* 打開瀏覽器，選擇Predict.ipynb
![](http://i.imgur.com/1VOpPd5.png)


* 在In[2]貼上想分析的文本，至```Cell```選擇```Run All```
![](http://i.imgur.com/FtgH93T.png)


* 範例結果
	* 新舊媒體的二元預測會顯示於圖表標題
	* 以字頻分布的相似度，對六家媒體作預測的結果以長條圖顯示
	![](http://i.imgur.com/mzgi6WP.png)

We are Group1 ! Enjoy it :smile:
