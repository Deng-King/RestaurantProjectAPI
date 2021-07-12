<template>
	<view>
		<u-cell-item hover-class='none' :arrow="false"  :value-style="vstyle" :title-style="tstyle" title="姓名" style="height: 130rpx;">{{infodata.user_name}}</u-cell-item>
		<u-cell-item hover-class='none' :arrow="false"  :value-style="vstyle" :title-style="tstyle" title="性别" style="height: 130rpx;">{{infodata.user_gender}}</u-cell-item>
		<u-cell-item hover-class='none' :arrow="false"  :value-style="vstyle" :title-style="tstyle" title="工号" style="height: 130rpx;">{{infodata.user_number}}</u-cell-item>
		<u-cell-item @click="position_show=true" :value-style="vstyle" :title-style="tstyle" title="职位" style="height: 130rpx;">{{infodata.user_position}}</u-cell-item>
		<u-cell-item @click="repwd" :value-style="vstyle" :title-style="tstyle" title="重置密码" style="height: 130rpx;"></u-cell-item>
		<u-button @click="button_click" class = "submit" type = "error">删除员工</u-button>
		<u-action-sheet @click="position_confirm" :list="positionlist" v-model="position_show"></u-action-sheet>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				infodata:{
					user_name:"张鑫",
					user_gender:"男",
					user_number:"20192997",
					user_position:"服务员"
				},
				tstyle:{
					'font-size': '40rpx',
					'font-weight': 'bold'
				},
				vstyle:{
					'font-size': '40rpx',
					'font-weight': 'bold',
					'margin-right': '25rpx'
				},
				position_show:false,
				positionlist: [
					{
						text: '服务员'
					},
					{
						text: '后厨'
					}
				],
				user_position:''
			}
		},
		methods: {
			position_confirm(index){
				this.user_position = this.positionlist[index].text
				console.log(this.user_position)
				if (this.user_position!=this.infodata.user_position){
					console.log("进行修改")
				}
			},
			button_click(){
				console.log("删除员工")
			},
			repwd(){
				console.log("重置密码")
			}
		}
	}
</script>

<style>
.input_item {
		margin-top: 20rpx;
		margin-left: 20rpx;
		margin-right: 20rpx;
		margin-bottom: 30rpx;
		display: flex;
		padding: 10rpx;
		border-color:#999999;
	}
	
.submit{
	margin: 50rpx 80rpx 50rpx 80rpx;
	height: 100rpx;
	font-size: 45rpx;
}
</style>
