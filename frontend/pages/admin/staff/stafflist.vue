<template>
	
	<view>

		<u-navbar :is-back="true" title="员工列表" backgroundColor ="#d34346">
			<u-col span="10"></u-col>
			<u-col span="2">
				<image src="../../../static/adder.png" style="width:70rpx; height:70rpx;margin-top: 10rpx;" @click="redirectadd()"></image>
				</u-col>
		</u-navbar>
		<table border="0" style="font-size: 35rpx; border-bottom: solid thin #EEEEEE;">
			<tr style="height:85rpx; background-color: #eaeaea;">
				<td class="td" style="width:250rpx;font-size: 45rpx;"> 工号</td>
				<td class="td" style="width:250rpx;font-size: 45rpx;"> 姓名</td>
				<td class="td" style="width:250rpx;font-size: 45rpx;"> 职务</td>
			</tr>
		</table>
		<u-swipe-action v-for="(item, index) in stafflist" :key=index :options="options"
			:btn-width="btnWidth" :show="item.show" @open="open(index)">
			<view>
				<table border="0" style="font-size: 35rpx; border-bottom: solid thin #EEEEEE;" >
					<tr style="height:85rpx;" @click="redirect()">
						<td class="td"> {{item.user_id}}</td>
						<td class="td"> {{item.loginname}}</td>
						<td class="td"> {{item.user_position}}</td>
					</tr>
				</table>
			</view>
		</u-swipe-action>
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
				btnWidth: 180,
				stafflist: [{
						user_id: 1237,
						loginname: "小明",
						user_position: "后厨",
						show:false,
						
					},
					{
						user_id: 1237,
						loginname: "小小明",
						user_position: "服务员",
						show:false,
					},
					{
						user_id: 1237,
						loginname: "小小小明",
						user_position: "管理员",
						show:false,
					},
					{
						user_id: 1237,
						loginname: "小明",
						user_position: "后厨",
						show:false,
					},
					{
						user_id: 1237,
						loginname: "小小明",
						user_position: "服务员",
						show:false,
					},
					{
						user_id: 1237,
						loginname: "小小小明",
						user_position: "管理员",
						show:false,
					},
					{
						user_id: 1237,
						loginname: "小明",
						user_position: "后厨",
						show:false,
					},
					{
						user_id: 1237,
						loginname: "小小明",
						user_position: "服务员",
						show:false,
					},
					{
						user_id: 1237,
						loginname: "小小小明",
						user_position: "管理员",
						show:false,
					},
					{
						user_id: 1237,
						loginname: "小明",
						user_position: "后厨",
						show:false,
					},
					{
						user_id: 1237,
						loginname: "小小明",
						user_position: "服务员",
						show:false,
					},
					{
						user_id: 1237,
						loginname: "小小小明",
						user_position: "管理员",
						show:false,
					},
					{
						user_id: 1237,
						loginname: "小小小明",
						user_position: "管理员",
						show:false,
					}],
				options: [{
						text: "删除",
						style: {
							backgroundColor: '#dd524d'
						}
					},
					{
						text: "修改",
						style: {
							backgroundColor: '#007aff'
						}
					}
				]
			}
		},
		methods: {
			open(index){
				this.stafflist[index].show=true;
				for(var i=0; i<this.stafflist.length; i++){
					if(i!=index){
						this.stafflist[i].show=false;
					}
				}
			},
			redirect(){
				uni.navigateTo({
					url: './stafflcontent/stafflcontent'
				});
			},
			redirectadd(){
				uni.navigateTo({
					url:'./staffadd/staffadd'
				})
			}
		},
		computed: {
			...mapGetters([
				'tabBarList'
			])
		},
		onShow(){
			for(var i=0; i<this.stafflist.length;i++){
				this.stafflist[i].show=false;
			}
		}
	}
</script>

<style>
	.td {
		width: 250rpx;
		text-align: center;
	}
</style>
