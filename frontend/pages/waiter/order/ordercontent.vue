<template>
	<view>
		<!-- 标题 -->
		<view style="text-align: center; border-style: solid;
					border-width: thin;border-color: #C0C0C0; height:90rpx; line-height: 90prx;">
			<text style="font-size: 30px;">菜品详情</text>
		</view>
		<image src="http://124.70.200.142:8080/img/food.png" mode="aspectFit" style="text-align: center;width:100%;"></image>
		<u-row gutter="12">
			<u-col span="1"></u-col>
			<u-col span="5">
				<text class="title">嫩牛五方</text>
			</u-col>
			<u-col span="2"></u-col>
			<u-col span="2"><text class="price">￥{{price}}</text></u-col>
		</u-row>
		<u-row gutter="0">
			<u-col span="1" style="background-color: #C0C0C0;"></u-col>
			<u-col span="10">
				<u-line color="#aeb8b9" />
			</u-col>
			<u-col span="1" style="background-color: #C0C0C0;"></u-col>
		</u-row>
		<u-row gutter="0">
			<u-col span="1" style="background-color: #C0C0C0;"></u-col>
			<u-col span="10">
				<text class="text">{{intro}}</text>
			</u-col>
			<u-col span="1" style="background-color: #C0C0C0;"></u-col>
		</u-row>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				intro: "“嫩牛五方”是肯德基曾出的一款的卷饼类快餐。牛肉蛋白质含量高，而脂肪含量低，所以味道鲜美，受人喜爱，享有“肉中骄子”的美称。",
				price: 20,
			}
		},
		methods: {
			connect() {
				uni.request({
					url: 'api/waiter/meals/list/details',
					method: 'GET',
					success: (res) => {
						//console.log(eval(res.data.data));
						this.noticelist = eval(res.data.data);
						console.log(res.data);
					}
				})
			}
		}
	}
</script>

<style>
	.title {
		font-size: 60rpx;
		font-weight: bold;
	}

	.text {
		font-size: 30rpx;
	}

	.price {
		color: #c21919;
		font-size: 60rpx;
		font-weight: bold;
	}
</style>
