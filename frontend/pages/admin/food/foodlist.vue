<template>
	<view>
		<!-- content -->
		<u-cell-group>
			<view v-for="(item,index) in contentlist" style="margin-top: 0rpx;">
			<u-cell-item>
				<u-row gutter="20">
				<u-col span="2.5" style="margin-left: 5rpx;">
					<image :src="item.url" mode="aspectFit" class="listimage" @click="click(index)"></image>
				</u-col>
				<u-col span="5" @click="click(index)">
						<u-row span="4">
							<text class="name">{{item.name}}</text>
						</u-row>
						<u-row span="2">
							<text class="price">￥{{item.price}}</text>
						</u-row>
				</u-col>
				<u-col span="2">
					<u-tag text="HOT!" shape="circle" type="error" :closeable="false" :show="item.hot" size="mini"> </u-tag>
				</u-col>
			</u-row>
			</u-cell-item>
			
		</view>
		</u-cell-group>
		<u-tabbar
			:list="tabBarList"
			active-color="#5098FF"
			inactive-color="#909399"
			:border-top= false
			bg-color = "#F8F8F8"
		></u-tabbar>
	</view>
</template>

<script>
	import { mapGetters } from 'vuex'
	export default {
		data() {
			return {
				contentlist: [{
						name: "嫩牛五方",
						url: "../../../static/food.png",
						value: 0,
						price: 20.55,
						hot: false,
					},
					{
						name: "嫩牛六方",
						url: "../../../static/food1.png",
						value: 0,
						price: 100.00,
						hot: true,
					},
					{
						name: "嫩牛五方",
						url: "../../../static/food1.png",
						value: 0,
						price: 5.00,
						hot: false,
					},
					{
						name: "嫩牛五方",
						url: "../../../static/food1.png",
						value: 0,
						price: 8.00,
						hot: false,
					},
					{
						name: "嫩牛五方",
						url: "../../../static/food1.png",
						value: 0,
						price: 9.00,
						hot: true,
					},{
						name: "嫩牛五方",
						url: "../../../static/food.png",
						value: 0,
						price: 20.55,
						hot: false,
					},
					{
						name: "嫩牛六方",
						url: "../../../static/food1.png",
						value: 0,
						price: 100.00,
						hot: true,
					},
					{
						name: "嫩牛五方",
						url: "../../../static/food1.png",
						value: 0,
						price: 5.00,
						hot: false,
					},
					{
						name: "嫩牛五方",
						url: "../../../static/food1.png",
						value: 0,
						price: 8.00,
						hot: false,
					},
					{
						name: "嫩牛五方",
						url: "../../../static/food1.png",
						value: 0,
						price: 9.00,
						hot: true,
					},{
						name: "嫩牛五方",
						url: "../../../static/food.png",
						value: 0,
						price: 20.55,
						hot: false,
					},
					{
						name: "嫩牛六方",
						url: "../../../static/food1.png",
						value: 0,
						price: 100.00,
						hot: true,
					},
					{
						name: "嫩牛五方",
						url: "../../../static/food1.png",
						value: 0,
						price: 5.00,
						hot: false,
					},
					{
						name: "嫩牛五方",
						url: "../../../static/food1.png",
						value: 0,
						price: 8.00,
						hot: false,
					},
					{
						name: "嫩牛五方",
						url: "../../../static/food1.png",
						value: 0,
						price: 9.00,
						hot: true,
					},{
						name: "嫩牛五方",
						url: "../../../static/food.png",
						value: 0,
						price: 20.55,
						hot: false,
					},
					{
						name: "嫩牛六方",
						url: "../../../static/food1.png",
						value: 0,
						price: 100.00,
						hot: true,
					}

				],
				money: 0,
				count: 0,
				currtable: 1,
			}
		},
		methods: {
			click(index) {
				console.log(index);
				uni.navigateTo({
					url: '../order/ordercontent/ordercontent'
				});
			},
			connect() {
				uni.request({
					url: 'api/waiter/meals/list',
					method: 'GET',
					success: (res) => {
						//console.log(eval(res.data.data));
						this.noticelist = eval(res.data.data);
						console.log(res.data);
					}
				})
			}
		},
		computed: {
			...mapGetters([
				'tabBarList'
			])
		}
	}
</script>

<style>
	.button {
		background-color: #d80000;
		color: #F8F8F8;
		border-radius: 40rpx;
		vertical-align: middle;
		height: 80rpx;
		line-height: 80rpx;
		font-weight: bold;
		font-size: 45rpx;
	}

	.footer {
		position: fixed;
		left: 0rpx;
		bottom: 0rpx;
		width: 100%;
	}

	.listitem {
		background-color: #C8C7CC;
		font-size: 50rpx;
	}

	.listimage {
		height: 120rpx;
		width: 150rpx;
		border-radius: 8rpx;
		border: #C8C7CC solid thin;
	}

	.list {
		display: flex;
		flex-direction: row;
	}

	.price {
		font-size: 35rpx;
		color: #de1212;
		font-weight: bold;
	}

	.name {
		font-size: 35rpx;
	}
</style>
