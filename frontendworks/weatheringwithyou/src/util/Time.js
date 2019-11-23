export default {
    getTime: function getTime(time){
        let dateTime = new Date(time);
        let y = this.zeroBu(dateTime.getFullYear());//年
        let m = this.zeroBu(dateTime.getMonth() + 1);//月
        let d = this.zeroBu(dateTime.getDate());//日
        let h = this.zeroBu( dateTime.getHours());//时
        let mm = this.zeroBu( dateTime.getMinutes());//分
        let s = this.zeroBu(dateTime.getSeconds());//秒
        let times=y+"-"+m+"-"+d+" "+h+":"+mm+":"+s;
        return times;
    },
    //补零函数
    zeroBu: function f(n) {
        if(n<10){
            return '0'+n;
        }else{
            return n
        }
    }
}