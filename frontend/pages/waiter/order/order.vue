<template>
	<view>
		<!-- 标题 -->
		<view style="text-align: left; margin-bottom: 10rpx;
					border-width: thin;border-color: #C0C0C0; ">
			<text
				style="font-size: 30px; ; margin-left: 20rpx; height:100rpx; line-height: 100prx;">当前桌号：{{currtable}}</text>
		</view>
		<!-- content -->
		<view v-for="(item,index) in contentlist" style="margin-top: 0rpx;">
			<u-row gutter="20" style="border: #C8C7CC solid 1rpx;">
				<u-col span="2.5" style="margin-left: 5rpx;">
					<image :src="item.url" mode="aspectFit" class="listimage" @click="click(index)"></image>
				</u-col>

				<u-col span="3.5" @click="click(index)">
					<u-col gutter="4">
						<u-row span="2">
							<text class="name">{{item.name}}</text>
						</u-row>
						<u-row span="2">
							<text class="price">￥{{item.price}}</text>
						</u-row>
					</u-col>
				</u-col>
				<u-col span="2">
					<u-tag text="HOT!" shape="circle" type="error" :closeable=false :show=item.hot size="mini"> </u-tag>
				</u-col>
				<u-col span="2">
					<u-number-box v-model="item.value" @minus="minus(index)" @plus="plus(index)" :disabled-input=true>
					</u-number-box>
				</u-col>
			</u-row>
		</view>

		<!-- 提交 -->
		<view class="footer"
			style="padding:10rpx; background-color: #000000; width:100%; color: #FFFFFF;border-radius:8px;">
			<u-row gutter="11">
				<u-col span="7" style="background-color: #030303; margin-right: 30rpx;">
					<text style="font-size: 60rpx; color: #C8C7CC;">共计：</text>
					<text style="font-size: 50rpx;" space="emsp">{{money}}元</text>
					<text style="font-size: 30rpx;" space="emsp">\n {{count}}项</text>
				</u-col>
				<u-col span="4" style="text-align: center;border-radius: 8rpx; ">
					<button class="button" @click="showToast()">提交</button>
					<u-toast ref="uToast" />
				</u-col>
			</u-row>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				contentlist: [{
						name: "嫩牛五方",
						url: "http://124.70.200.142:8080/img/food.png",
						value: 0,
						price: 20.55,
						hot: false,
					},
					{
						name: "张诗琦",
						url: "http://124.70.200.142:8080/img/food.png",
						value: 0,
						price: 100.00,
						hot: true,
					},
					{
						name: "嫩牛五方",
						url: "http://124.70.200.142:8080/img/food.png",
						value: 0,
						price: 5.00,
						hot: false,
					},
					{
						name: "嫩牛五方",
						url: "http://124.70.200.142:8080/img/food.png",
						value: 0,
						price: 8.00,
						hot: false,
					},
					{
						name: "嫩牛五方",
						url: "http://124.70.200.142:8080/img/food.png",
						value: 0,
						price: 9.00,
						hot: true,
					},

				],
				money: 0,
				count: 0,
				currtable: 1,
			}
		},
		methods: {
			minus(index) {
				this.count -= 1;
				this.money -= this.contentlist[index].price;
				this.money = Math.round(this.money * 100) / 100;
			},
			plus(index) {
				this.count += 1;
				this.money += this.contentlist[index].price;
				this.money = Math.round(this.money * 100) / 100;
			},
			showToast() {
				if (this.count == 0) {
					this.$refs.uToast.show({
						title: '请添加菜品',
						type: 'error',
						url: '/pages/order/order'
					})
				} else {
					this.$refs.uToast.show({
						title: '提交成功',
						type: 'success',
						url: '/pages/order/order'
					})
				}
			},
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

	.name {}
</style>
