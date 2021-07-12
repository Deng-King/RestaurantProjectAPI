<template>
	<view style="margin: 20rpx;">
		<view  class="line">
			<u-row>
				<u-col span="3" >
					<view style="color: #2C405A; font-size: 40rpx; font-weight: bold; margin-left: 35rpx;">菜名</view>
				</u-col>
				<u-col span="8.5">
					<u-input  :customStyle="cstyle" style="  margin-top: 10rpx;  height: 80rpx;"></u-input>
				</u-col>
			</u-row>
		</view>
		
		<view  class="line">
			<u-row>
				<u-col span="3" >
					<view style="color: #2C405A; font-size: 40rpx; font-weight: bold; margin-left: 35rpx;">
						<text >简介</text>
					</view>
				</u-col>
				<u-col span="8.5" >
					<u-input :auto-height ="true"  type="textarea" :customStyle="cstyle" style=" margin-top: 10rpx; "></u-input>
				</u-col> 

				<u-col>
					<view>
						<u-cell-item :title-style="tstyle" title="配图" style="margin-top: 20rpx;">

						</u-cell-item>
					</view>
				</u-col>
				<u-col>
					<view  style=" margin-top: 30rpx; margin-bottom: 30rpx;">
						<u-row>
							<u-col span="3">
								<text style="color: #2C405A; font-size: 40rpx; font-weight: bold; margin-left: 20rpx;">金额</text>
							</u-col>
							<u-col span="4">
								<u-input style=" text-align: end;" placeholder="00" border="" maxlength="5"></u-input>
							</u-col>
							<u-col  span="0.5">
								<text style="font-size: 50rpx;">.</text>
							</u-col>
							<u-col  span="3">
								<u-input placeholder="00" border="" maxlength="2"></u-input>
							</u-col>
						</u-row>
					</view>
					<view>
						<u-cell-item :title-style="tstyle" title="推荐" style="margin-top: 20rpx;">
					
						</u-cell-item>
					</view>
				</u-col>
				<u-button type="primary" style="width: 80%; margin-top: 100rpx;font-size: 40rpx;">提交</u-button>
			</u-row>
		</view>
		
		


		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				cstyle: {
					'font-size':"40rpx"
					
				},
				tstyle:{
					'font-size': '40rpx',
					'font-weight': 'bold'
				},
				money:''
			}
		},
		methods: {
			click(index){
				console.log(index);
			}
			// testMoney(e) {
			//     let amount = e.detail.value;
			// 	amount= /(^[1-9]([0-9]+)?(\.[0-9]{1,2})?$)|(^(0){1}$)|(^[0-9]\.[0-9]([0-9])?$)/.test(amount) ? amount : amount.substring(0,amount.length-1)
			// 	setTimeout(() => {
			// 		this.money = Number(amount);
			// 	}, 1);
			//  }
			
			// testMoney(e){
			//                 let that = this;
			//                 let price = e.detail.value
			//                 if (price.indexOf(".") == 0) {
			//                     //'首位小数点情况'
			//                     price = price.replace(/[^$#$]/g, "0.");
			//                     price = price.replace(/\.{2,}/g, ".");
			//                 } 
			//                 price = price.match(/^\d*(\.?\d{0,2})/g)[0] || null;
			//                   //重新赋值给input
			//                 this.$nextTick(() => {
			//                     this.money = price;
			//                 });
			 
			
		}
	}
</script>
	
<style>
.line{
	height: 100rpx;
	/* background-color: #cecece; */
	border-bottom: #606266;
	margin-bottom: 10rpx;
	margin-top: 10rpx;
}
</style>
