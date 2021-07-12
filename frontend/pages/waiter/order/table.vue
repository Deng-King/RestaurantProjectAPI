<template>
	<view>
		<view style="margin-left: 55rpx;">
			<u-row >
				<view v-for="(item, index) in tablelist" >
					<u-col span="1">
						<u-button v-if="item.table_state===0" type="success" class="button" @click="click(index)">
							<view style="flex-direction: column;">
								<view style="height: 55rpx;">桌 号</view>
								<view style="height: 55rpx;font-size: 60rpx;">{{item.table_id}}</view>
								<view style="height: 80rpx;font-size: 35rpx;">空闲</view>
							</view>
						</u-button>
						
						<u-button v-if="item.table_state===1" type="warning" class="button" @click="click(index)">
							<view style="flex-direction: column;">
								<view style="height: 55rpx;">桌 号</view>
								<view style="height: 55rpx;font-size: 60rpx;">{{item.table_id}}</view>
								<view style="height: 80rpx;font-size: 35rpx;">用餐中</view>
							</view>
						</u-button>
					</u-col>
				</view>
			</u-row>
		</view>
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
				tablelist:[
					{
						table_id:1,
						table_state:1
					},
					{
						table_id:2,
						table_state:1
					},
					{
						table_id:3,
						table_state:0
					},
					{
						table_id:4,
						table_state:0
					},
					{
						table_id:5,
						table_state:1
					},
					{
						table_id:6,
						table_state:0
					},
					{
						table_id:7,
						table_state:0
					}
				]
			}
		},
		methods: {
			click(index){
				console.log(index);
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
.table{
	margin: 20rpx;
	/* display: block; */
	
}
.button{
	width: 160rpx;
	height: 160rpx;
	margin: 20rpx;
	border-radius: 20rpx;
}
.u-row {
	margin: 40rpx 0;
}
</style>
