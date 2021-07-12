<template>
	<view>
		<!-- 几个设置的cell -->
		<u-cell-item @click="name_show=true" :value-style="vstyle" :title-style="tstyle" title="姓名" style="height: 130rpx;">{{user_name}}</u-cell-item>
		<u-cell-item @click="gender_show=true" :value-style="vstyle" :title-style="tstyle" title="性别" style="height: 130rpx;">{{user_gender}}</u-cell-item>
		<u-cell-item @click="number_show=true" :value-style="vstyle" :title-style="tstyle" title="工号" style="height: 130rpx;">{{user_number}}</u-cell-item>
		<u-cell-item @click="position_show=true" :value-style="vstyle" :title-style="tstyle" title="职位" style="height: 130rpx;">{{user_position}}</u-cell-item>
		<!-- 姓名模态框 -->
		<u-modal  v-model="name_show"  @confirm="user_name=name"  title="设置姓名" :show-cancel-button="true">
			<view class="input_item">
				<u-input height="80" :placeholder = "user_name"  v-model="name" type='text' :border="true"/>
			</view>
		</u-modal>

		<!-- 性别表单 -->
		<u-action-sheet @click="gender_confirm" :list="genderlist" v-model="gender_show"></u-action-sheet>

		<!-- 工号模态框 -->
		<u-modal  v-model="number_show"  @confirm="user_number= number"  title="设置工号" :show-cancel-button="true">
			<view class="input_item">
				<u-input height="80" :placeholder = "user_number"  v-model="number" type='text' :border="true"/>
			</view>
		</u-modal>
		<!-- 职位表单 -->
		<u-action-sheet @click="position_confirm" :list="positionlist" v-model="position_show"></u-action-sheet>
		
		<!-- 提交按钮 -->
		<u-button class = "submit" type = "primary">添加员工</u-button>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				tstyle:{
					'font-size': '40rpx',
					'font-weight': 'bold'
				},
				vstyle:{
					'font-size': '40rpx',
					'font-weight': 'bold',
					'margin-right': '25rpx'
				},
				// 绑定input框
				name:'',
				gender:'',
				number:'',
				position:'',
				// 绑定显示,也是最后发送的数据
				user_name:'',
				user_gender:'',
				user_number:'',
				user_position:'',
				// 显示哪一个膜态框
				name_show:false,
				gender_show:false,
				number_show:false,
				position_show:false,
				positionlist: [
					{
						text: '服务员'
					},
					{
						text: '后厨'
					}
				],
				genderlist: [
					{
						text: '男'
					},
					{
						text: '女'
					}
				]
			}
		},
		methods: {
			gender_confirm(index){
				this.user_gender = this.genderlist[index].text
			},
			position_confirm(index){
				this.user_position = this.positionlist[index].text
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
	margin: 80rpx;
	height: 100rpx;
	font-size: 45rpx;
}
</style>
