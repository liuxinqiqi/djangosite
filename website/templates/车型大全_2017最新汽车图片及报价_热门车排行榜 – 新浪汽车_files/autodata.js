var leftMenu = $("#J_motoDataNav");                         //��ർ��ȫ������
// var topHeight = 223;                                        //��ർ�����봰���ϱ�Ե��Ĭ�Ͼ��� (����������ʱ��243)
var newNavHeight = 0;
if($("#mainNav").prev().attr("class") == "global-head"){ newNavHeight = $("#mainNav").height() + 1;}
var topHeight = $(".global-head").height() + newNavHeight + 20;
var scrollLeterTop = $("#J_scrollLeter").offset().top;
var scrollLeterHeight = $(window).height() - $("#J_cataLeters").height() - 12 - 4;          //���ڸ߶�-��ĸ�������߶�-���12-�߿�߶�4

//Ĭ�Ϻ�����style����д���������û�������������ţ���ർ���߶����ã���˸߶��йغ���ȫ������
var resizeWindow = function(){
    $(window).resize(function(){
        scrollLeterHeight = $(window).height() - $("#J_cataLeters").height() - 12 - 4;
        resetNavHeightClassLast();
        resetLeterLast();
    });
}

//Ĭ�Ϻ�����style����д��������sidebar����&���ض���
var sidebarPosition = function(){
    // �������
    var DocHeight,WinWidth,WinHeight,DocScroll,popWidth,popHeight,popLeft,popTop;
    var contentWidth = jQuery(".wrap:first").width();
    //У����������ʾλ��
    function correctPopupState(popElement){
        DocHeight = parseInt(jQuery(document).height());
        WinWidth = parseInt(jQuery(window).width());
        WinHeight = parseInt(jQuery(window).height());
        DocScroll = parseInt(jQuery(document).scrollTop());
        popWidth = parseInt(jQuery(popElement).width());
        popHeight = parseInt(jQuery(popElement).height() + 80);
        popRight = parseInt((WinWidth-contentWidth)/2 - 10 - 40);
        popTop = parseInt(WinHeight-popHeight);
        popRight = popRight > 10?popRight:10;
        popTop = popTop > 0?popTop:0;
        jQuery(popElement).css({"display":"block","z-index":"10000","right":popRight - 20});
        if(DocScroll == 0){
            jQuery(popElement).find('.return_top').hide();
        } else {
            jQuery(popElement).find('.return_top').show();
        }
        if(!-[1,]&&!window.XMLHttpRequest){
            jQuery(popElement).css({"top":DocScroll+popTop+"px"});
        }
    }
    jQuery(window).load(function(){
        if(jQuery("#sidebar").length == 1){
            correctPopupState("#sidebar");
        }
    });
    //���Ŵ��ڸ��ĵ���λ��
    jQuery(window).resize(function(){
        if(jQuery("#sidebar").length == 1){
            correctPopupState("#sidebar");
        }
    });
    //�϶�������
    jQuery(window).scroll(function(){
        if(jQuery("#sidebar").length == 1){
            correctPopupState("#sidebar");
        }
    });
    jQuery("#sidebar .return_top").click(function(){
        jQuery("body,html").animate({"scrollTop":0},800);
    });
    jQuery('#sidebar').find('.show_code').hover(function(){
        jQuery(this).find('.code').show();
    },function(){
        jQuery(this).find('.code').hide();
    });
}

//Ĭ�Ϻ�����style����д��������tab�л�����
var tabExchange = function(elem,hover){
    elem.hover(function(){
        var idx = $(this).index();
        $(this).addClass(hover).siblings().removeClass(hover);
        $(this).parent().next().children().eq(idx).show().siblings().hide();
    });
}

//Ĭ�Ϻ�����style����д����������껬����ť����
var btnHighLight = function(elem,hover){
    elem.hover(function(){
        $(this).addClass(hover);
    },function(){
        $(this).removeClass(hover);
    });
}

//Ĭ�Ϻ�����style����д���������ʴ���ȡ��ʧȥ����
var textFocusBlur = function(elem,focus){
    elem.focus(function(){
        if($(this).val() == this.defaultValue){
            $(this).addClass(focus).val("");
        }
    }).blur(function(){
        if ($(this).val() == "") {
            $(this).removeClass(focus).val(this.defaultValue);
        }
    });
}

//Ĭ�Ϻ�����style����д��������ָ�����ݿ���չ������
var slideBtnDown = function(elem,target){
    elem.live("click",function(){
        target.slideToggle("fast");
        elem.parent().toggleClass("show");
    });
}

//����������style�������ݡ�������������main��λ������
var resetBodyScrollTop = function(){
    var bodyScrollTop = $("body,html").scrollTop();
    if(bodyScrollTop != topHeight){
        $("body,html").animate({"scrollTop":topHeight},300);
    }
}

//����������style�������ݡ�������������main��λ��ɸѡ��
// var resetBodyScrollMiddle = function(){
//     var bodyScrollTop = $("body,html").scrollTop(),
//         middleHeight = $("#J_imgFilterLable").offset().top;
//     if(bodyScrollTop != middleHeight){
//         $("body,html").animate({"scrollTop":middleHeight},300);
//     }
// }

//����������style�������ݡ�������J_dtHeight��dt�߶ȵ��ڸ����߶�
var resetDtHeight = function(){
    $(".J_dtHeight").each(function(){
        // $(this).children("dt").css("height","auto"); //��Ӧ����ҳ����ڲ�ͣ����������ת����tab�л�ʱ
        $(this).find("dt").css("height",$(this).children("dl").height());
        $(this).css("height","auto");
        $(this).find("dd.in-p a, dd.stop-p a").css("opacity","1");
        //�ٴ���һ�����ֲ������ر��ļ��������
        $(this).find("dt").css("height",$(this).children("dl").height());
    });
}

//����������style�������ݡ���������ȡ�û����ڳߴ磬�Ա�ȷ������������ĸ���߶ȣ�J_scrollClass�����һ��li��padding���Ա��ܶ�λ������
var resetNavHeightClassLast = function(){
    $("#J_scrollLeter").css("height", scrollLeterHeight);
}

//����������style�������ݡ�������J_scrollLeter�����һ��li��padding���Ա��ܶ�λ������
var resetLeterLast = function(){
    var makerLast = $("#J_scrollLeter").find("li").last();
    makerLast.css("padding-bottom", scrollLeterHeight - makerLast.height());
}

//����������style�������ݡ�������J_cataLeters�л�ȡ��ǰѡ�е���ĸ���Ա�J_scrollLeter�ж�ӦƷ���ܶ�λ������
var resetLeterInitPos = function(){
    var letterCurrent = $("#J_cataLeters").find("a.on").attr("data-name");
    if(letterCurrent){
        var classCurrentTop = $("#J_scrollLeter").find("h5[data-name='"+ letterCurrent +"']").offset().top;
        $("#J_scrollLeter").scrollTop(classCurrentTop - scrollLeterTop + $("#J_scrollLeter").scrollTop());
    }
}

//ҳ���ʼ������
var initPage = function(){
    //��������Ӧ��������ɸѡ����dt�߶ȼ���
    if($('.para-filtru').length > 0){
        resetDtHeight();
    }
    //��������Ӧ���ڵ�ǰѡ�г���ҳ��ĵ�����������λ
    // if($('#J_isProSale').length > 0){
    //     var dataCurrent = $('#J_cataLeters').find('.current').attr("data-name"),
    //         classCurrentTop = $("#J_scrollLeter").find("h5[data-name='"+ dataCurrent +"']").offset().top;
    //     $('#J_scrollLeter').scrollTop(classCurrentTop - scrollLeterTop + $("#J_scrollLeter").scrollTop());
    // }
    resetNavHeightClassLast();
    resetLeterInitPos();
    //����ѡ������Ӧ�ù��������
    $('#J_scrollLeter').perfectScrollbar();
    //����ɸѡ����Ӧ�ù��������
    $('#J_scrollCity').perfectScrollbar();
    //Ĭ���¼�����ӣ��������۽� etc.
    resizeWindow();
    sidebarPosition();
    tabExchange($(".tab-tit a"),"on");
    btnHighLight($("#J_searchKeyword"),"hover");
    textFocusBlur($("#J_cText"),"focus");
    slideBtnDown($("#J_furlBtn"),$("#J_furlOthers"));
}
initPage();

//����ͼ�л�Ч��
/*
imgsCon  //�˶�Ԫ�ص�id��class
iconsCon  //������ť��Ԫ�ص�id��class
prevIcon  //��ǰ��ť��Ԫ�ص�id��class
nextIcon   //���ť��Ԫ�ص�id��class
chooseIcon   //��ť��ѡ��ʱ���ӻ�ɾ����class  Ĭ����on
focusNum  //������ʾ��ǰ�ڼ�ҳ��Ԫ�ص�id��class
moveTime  //�����˶�ʱ��  Ĭ��800����
delayTime  //�����ӳ�ʱ��  Ĭ��5000����
isAuto  //�Ƿ��Զ��ֻ�  Ĭ�ϲ��Զ�
isCycle  //�Ƿ��˶���ͷ����ѭ��  Ĭ�ϲ�ѭ��
isSingleImg // �ǵ�ͼˢ���ֻ����Ƕ�ͼˢˢˢ���ֻ� Ĭ����ˢˢˢ���ֻ�
direction //�˶����� Ĭ����ˮƽ�˶�
step //ÿ���ֵĲ��� Ĭ����1
imgDescDom //���ڴ��ͼƬ������Ϣ��id��class
cannotClickClass //���Ҳ��ܵ��ʱ�ӵ�class Ĭ�ϼ�end
beginPos //��������ʼλ�ò���left 0 ���˶� Ĭ����0
*/
function autoMove(options) {
    var $imgs_c = $(options.imgsCon),
        $icons_c = $(options.imgsCon).parent().parent().find(options.iconsCon),
        $imgs = $imgs_c.children(),
        $icons = $icons_c.children(),
        iconsTagName = $icons.eq(0).get(0) ? $icons.eq(0).get(0).tagName.toLowerCase() : 'li',
        $imgDescDom = $(options.imgDescDom),
        $prevIcon = $(options.imgsCon).parent().parent().find(options.prevIcon),
        $nextIcon = $(options.imgsCon).parent().parent().find(options.nextIcon),
        chooseIcon = options.chooseIcon ? options.chooseIcon : 'on',
        step = options.step ? options.step : 1,
        cannotClickClass = options.cannotClickClass || 'end',
        moveTime = options.moveTime ? options.moveTime : 800,
        delayTime = options.delayTime ? options.delayTime : 5000,
        isSingleImg = options.isSingleImg ? options.isSingleImg : false,//�Ƿ��ǵ�ͼˢ���ֻ���Ĭ����ˢˢˢ���ֻ�
        isAuto = options.isAuto ? options.isAuto : false,
        isCycle = options.isCycle ? options.isCycle : false,
        directionData = {},
        direction = options.direction ? options.direction : 'left',
        moveDistance = direction === 'left' ? $imgs.eq(0).outerWidth(true) : $imgs.eq(0).outerHeight(true),
        beginPos = options.beginPos ? options.beginPos : 0,
        $focusNum,
        page = 0,
        moveTimer = null,
        showImgLen = $imgs.length,
        move;

    if (options.focusNum) {
        $focusNum = $(options.focusNum);
    }

    if (showImgLen === step) {
        $prevIcon.addClass(cannotClickClass);
        $nextIcon.addClass(cannotClickClass);
        return;
    } else if (step == 1 && isCycle && !isSingleImg) {
        $imgs_c.append($imgs.eq(0).clone(true));
        if (direction === 'left') {
            $imgs_c.width(moveDistance * (showImgLen + 1));
        }      
    } else if (!isSingleImg) {
        if (direction === 'left') {
            $imgs_c.width(moveDistance * showImgLen);
        }
    } else if (isSingleImg) {
        $imgs.eq(0).css(direction, '0px');
    }

    move = function(){
        window.clearTimeout(moveTimer);
        if (!$imgs_c.is(':animated') && !isSingleImg) {
            page++;         
            if (page === Math.ceil(showImgLen / step) && isCycle) {
                if ($focusNum) {
                    $focusNum.html(1);
                }
                $imgs_c.next().children().eq(0).addClass(chooseIcon).siblings().removeClass(chooseIcon);
                directionData[direction] = beginPos - moveDistance * step * page;
                $imgs_c.stop().animate(directionData, moveTime, function () {
                    $imgs_c.css(direction, beginPos + 'px');
                    page = 0;
                    if (options.callback) {
                        options.callback(page);
                    }
                    if (isAuto) {
                        moveTimer = window.setTimeout(move, delayTime);
                    }
                });
            } else if (page === Math.ceil(showImgLen / step) && !isCycle) {
                page--;
                return;
            } else {
                if ($focusNum) {
                    $focusNum.html(page + 1);
                }
                directionData[direction] = beginPos - moveDistance * step * page;
                $imgs_c.stop().animate(directionData, moveTime, function() {
                    if (options.callback) {
                        options.callback(page);
                    }
                    if (page + 1 === Math.ceil(showImgLen / step) && !isCycle) {
                        $nextIcon.addClass(cannotClickClass);
                    }
                });
                $imgs_c.next().children().eq(page).addClass(chooseIcon).siblings().removeClass(chooseIcon);
                if (isAuto) {
                    moveTimer = window.setTimeout(move, delayTime);
                }
            }
        } else if (!$imgs.eq(page).is(':animated') && isSingleImg) {
            page++; 
            if (page === showImgLen) {
                page = 0;
                directionData[direction] = beginPos - moveDistance;
                $imgs.eq(showImgLen - 1).stop().animate(directionData, moveTime);
            } else {
                directionData[direction] = beginPos - moveDistance;
                $imgs.eq(page - 1).stop().animate(directionData, moveTime);
            }
            directionData[direction] = beginPos;
            $imgs.eq(page).css(direction, moveDistance).stop().animate(directionData, moveTime);
            $imgs_c.next().children().eq(page).addClass(chooseIcon).siblings().removeClass(chooseIcon);
            if (isAuto) {
                moveTimer = window.setTimeout(move, delayTime);
            }
        }
    };

    if (isAuto) {
        moveTimer = window.setTimeout(move, delayTime);
    }

    $imgs_c.delegate($(this).children(), 'mouseover', function (e) {
            window.clearTimeout(moveTimer);
    });

    $imgs_c.delegate($(this).children(), 'mouseout', function (e) {
        if (isAuto) {
            moveTimer = window.setTimeout(move, delayTime);
        }
    });

    $icons_c.delegate(iconsTagName, 'mouseover', function (e) {
        window.clearTimeout(moveTimer);
        if (!isSingleImg) {            
            page = $(e.target).index();
            if ($focusNum) {
                $focusNum.html(page + 1);
            }
            directionData[direction] = beginPos - moveDistance * step * page;
            $imgs_c.stop().animate(directionData, moveTime, function() {
                if (options.callback) {
                    options.callback(page);
                }
            });
            $(e.target).addClass(chooseIcon).siblings().removeClass(chooseIcon);
        } else if (isSingleImg && $(e.target).index() !== page) {
            if (page > $(e.target).index()) {//��˳��С�ڵ�ǰ�İ�ť
                $imgs.eq($(e.target).index()).css(direction, beginPos - moveDistance);
                directionData[direction] = moveDistance - beginPos;
                $imgs.eq(page).stop(false, true).animate(directionData, moveTime);
                page = $(e.target).index();
                directionData[direction] = beginPos;
                $imgs.eq(page).stop().animate(directionData, moveTime);
                $(e.target).addClass(chooseIcon).siblings().removeClass(chooseIcon);
            } else {
                directionData[direction] = beginPos - moveDistance;
                $imgs.eq(page).stop(false, true).animate(directionData, moveTime);
                page = $(e.target).index();
                directionData[direction] = beginPos;
                $imgs.eq(page).css(direction, moveDistance).stop().animate(directionData, moveTime);
                $(e.target).addClass(chooseIcon).siblings().removeClass(chooseIcon);
            }
        }
    });

    $icons_c.delegate(iconsTagName, 'mouseout', function (e) {
        if (isAuto) {
            moveTimer = window.setTimeout(move, delayTime);
        }
    });

    $prevIcon.click(function() {
        $(this).next().removeClass(cannotClickClass);//$nextIcon
        if (page === 0 && !isCycle && !isSingleImg) {
            return;
        } else {
            window.clearTimeout(moveTimer);
            if (!$imgs_c.is(':animated') && !isSingleImg) {
                page--;
                if (page === -1) {
                    $imgs_c.css(direction, beginPos - moveDistance * step * showImgLen + 'px');
                    page = showImgLen - 1;
                }
                if ($focusNum) {
                    $focusNum.html(page + 1);
                }
                directionData[direction] = beginPos - moveDistance * step * page;
                $imgs_c.stop().animate(directionData, moveTime, function() {
                    if (options.callback) {
                        options.callback(page);
                    }
                    if (page === 0 && !isCycle) {
                        $prevIcon.addClass(cannotClickClass);
                    }
                });
                $imgs_c.next().children().eq(page).addClass(chooseIcon).siblings().removeClass(chooseIcon);
                if (isAuto) {
                    moveTimer = window.setTimeout(move, delayTime);
                }
            } else if (!$imgs.eq(page).is(':animated') && isSingleImg) {
                page--;
                if (page === -1) {
                    page = showImgLen - 1;
                    $imgs.eq(page).css(direction, beginPos - moveDistance);
                    directionData[direction] = moveDistance - beginPos;
                    $imgs.eq(0).stop(false, true).animate(directionData, moveTime);
                } else {
                    $imgs.eq(page).css(direction, beginPos - moveDistance);
                    directionData[direction] = moveDistance - beginPos;
                    $imgs.eq(page + 1).stop(false, true).animate(directionData, moveTime);
                }
                directionData[direction] = beginPos;
                $imgs.eq(page).stop().animate(directionData, moveTime);
                $imgs_c.next().children().eq(page).addClass(chooseIcon).siblings().removeClass(chooseIcon);
                if (isAuto) {
                    moveTimer = window.setTimeout(move, delayTime);
                }
            }
        }
    });

    $nextIcon.click(function() {    
        $(this).prev().removeClass(cannotClickClass);//$prevIcon
        if (page === showImgLen - 1 && !isCycle && !isSingleImg) {
            return;
        } else {
            move();
        }
    });
}

$(function () {
    //����ͼЧ��
    // $.getJSON('http://photo.auto.sina.com.cn/interface/v2/general/get_index_focus.php?callback=?', function(data) {
    //     if (data.result.status.code == 0 && data.result.data) {
    //         var data = data.result.data,
    //             len = data.length,
    //             tmpHtml = '',
    //             orderHtml = '';
    //         for (var i = 0; i < len; i++) {
    //             tmpHtml += '<li><a href="'+ data[i].url +'" target="_blank"><img alt="'+ data[i].title +'" src="'+ data[i].img +'"></a></li>';
    //             var m = !i ? 'class="on"' : '';
    //             orderHtml += '<li '+ m +'></li>';
    //         }
    //         $('#lp_aside').html('');
    //         $('#lp_icons').html('');
    //         $('#lp_aside').append(tmpHtml);
    //         $('#lp_icons').append(orderHtml);
            // �ֲ�
            $('#lp_icons').css('marginLeft', - $('#lp_icons').width() / 2 +'px');
            autoMove({
                'imgsCon': '#lp_aside',
                'iconsCon': '#lp_icons',
                'prevIcon': '#lp_prevIcon',
                'nextIcon': '#lp_nextIcon',
                'chooseIcon': 'on',
                'isAuto': true,
                'isCycle': true,
                'moveTime': 300,
                'beginPos': -497
            });
            $('#lp_aside').children().eq(0).before($('#lp_aside').children().eq($('#lp_aside').children().length - 2).clone(true));
            $('#lp_aside').append($('#lp_aside').children().eq(2).clone(true));
            $('#lp_aside').width(600 * $('#lp_aside').children().length);
    //     }
    // });

    //������ҳ��ʱ���ص��¼���Ӧ���ڵ�����main����Ļ����أ�
    $(window).on('scroll', function () {
        var navScroll = $(document).scrollTop(),
            menuTop = leftMenu.offset().top,
            menuHeight = leftMenu.height();
        if (navScroll > topHeight) {
            leftMenu.css('position', 'fixed');
            leftMenu.css('top', '0');
            if ($.browser.msie && ($.browser.version == "6.0") && !$.support.style) {
                leftMenu.css('position', 'absolute');
                leftMenu.css('top', navScroll);
            }
        } else {
            leftMenu.css('position', 'static');
            leftMenu.css('top', '0');
        }
        $("#J_scrollLeter").css("height", scrollLeterHeight);
        scrollLeterTop = $("#J_scrollLeter").offset().top;
    });

    //����Ч����������̡���������Ϊѡ��״̬��������չ��
    $("#J_scrollLeter").find("dt > a").live("click",function () {
        if($(this).parent().hasClass("current")){
            $(this).parents("dl").removeClass("unfold");
        } else {
            $(this).parents("dl").addClass("unfold");
        }
    });

    //����Ч�����������+ ��������������չ��
    $("#J_scrollLeter").find("dt > b").live("click",function () {
        $(this).parents("dl").toggleClass("unfold");
    });

    //����Ч���������ĸ������������ê�㵽��Ӧ��ĸ����
    $("#J_cataLeters a:not(.no)").live("click",function(){
        $(this).addClass("on").siblings().removeClass("on");
        resetLeterInitPos();
    });

    //ͼ����Ʒ��ҳ����ɸѡ���ࡪ������Ҫ��Ӧչʾѡ�еĲ���/�ڲ�/ͣ������
    // $(".J_furlTab").click(function(){
    //     if($(this).hasClass("tit-in")){
    //         $(this).parent().find("dd.stop-p").hide();
    //         $(this).parent().find("dd.in-p").show();
    //         $(this).addClass("on").siblings().removeClass("on");
    //     } else if($(this).hasClass("tit-stop")){
    //         $(this).parent().find("dd.in-p").hide();
    //         $(this).parent().find("dd.stop-p").show();
    //         $(this).addClass("on").siblings().removeClass("on");
    //     } else {
    //         $(this).parent().find("dd").show();
    //         $(this).addClass("on").siblings().removeClass("on");
    //     }
    //     resetDtHeight();
    // });

    //commonFoot �ؼ���������ת
    $("#J_searchKeyword" ).click(function(){
        var valText = $("#J_cText" ).val();
        if( valText != "" ){
            window.open("http://db.auto.sina.com.cn/search/?search_txt=" + encodeURIComponent(valText));
        } else {
            window.open("http://db.auto.sina.com.cn/search/");
        }
    });

    // �����л�
    function TabFuc(tab,con,evt){
        var evt = evt || 'click';
        tab.children().on(evt,function(e){
            e.preventDefault();
            var idx = $(this).index();
            var children = con.children();
            $(this).addClass('on').siblings().removeClass('on');
            children.hide();
            children.eq(idx).show();

        })
    }
    TabFuc($('.ft-tab-hd'),$('.ft-tab-con'),'hover');

    if(typeof(cal_nude_price) != "undefined" && typeof(cal_displacement) != "undefined" && typeof(cal_seat_count) != "undefined"){
        //����������
        var cal_parms={
            //�㳵��
            nude_price:cal_nude_price || 100000,
            //����
            displacement:cal_displacement || 1.6,
            //��λ��
            seat_count:cal_seat_count || 5,
            //�������Ʒ���
            license:500,
            //�����������⸶���
            three_price:100000,
            //��ʻ�����⸶���
            driver_price:50000,
            //�˿����⸶���
            passenger_price:50000,
            //�������⸶���
            scratch_price:2000,
            //�����գ����� 1������ 0��
            is_import:0,
            //���ڱ���
            pay_percent:0.3,
            //��������
            pay_year:3,
            //����ѡ��
            insurance:{
                //������ʧ��
                ins_damage:1,
                //������������
                ins_three:1,
                //������Ա������-��ʻ��
                ins_driver:1,
                //������Ա������-�˿�
                ins_passenger:1,
                //ȫ��������
                ins_steal:1,
                //��ȼ��ʧ��
                ins_burn:1,
                //��������
                ins_scratch:1,
                //����������Լ��
                ins_deduction:1,
                //��������������
                ins_glass:1
            }
        };
        //������
        var cal=new Calculator;
        cal.getCalculator(cal_parms);
        //����ȫ����ܶ�ʹ�����¹�
        $('#J_allBuycar').find('.price').html(parseInt(cal.getPriceSum()/100)/100+'��');
        $('#J_loanBuycar').find('.price').html(cal.getPayment()+'/��');
    }

    //����ͼ�������
    if($('#chartBox').length && typeof(chartObj) != "undefined"){
        $('#chartBox').highcharts(chartObj);
    }

    //��������ʡ��ɸѡ����
    function bindMouse(elem,target){
        var _hideTimer;
        elem.mouseenter(function(){
            var popTop = $(this).offset().top,
                popLeft = $("#J_motoDataMain").offset().left;
            target.css({'top': popTop + 28,'left': popLeft}).slideDown(150);
            $("#J_scrollCity").scrollTop(0);
            $("#J_scrollCity").perfectScrollbar("update");
        });
        elem.mouseleave(function(){
            _hideTimer = setTimeout(function(){
                target.hide();
            },180);
        });
        target.mouseenter(function(){
            clearTimeout(_hideTimer);
            target.show();
        });
        target.mouseleave(function(){
            target.hide();
        });
    }
    bindMouse($(".J_cityChange"),$("#J_cityList"));
    bindMouse($(".J_provinceChange"),$("#J_provinceList"));
    $("#J_cityList .close").click(function(){
        $("#J_cityList").hide();
    });
    $("#J_cityLeters a").live("click",function(){
        $(this).addClass("on").siblings().removeClass("on");
        var letterCurrent = $("#J_cityLeters").find("a.on").attr("data-name");
        if(letterCurrent){
            var classCurrentTop = $("#J_scrollCity").find(".tit[data-name='"+ letterCurrent +"']").parent().offset().top;
            $("#J_scrollCity").scrollTop(classCurrentTop - $("#J_scrollCity").offset().top + $("#J_scrollCity").scrollTop());
        }
    });

    if(typeof(brand_id) != "undefined" && typeof(bid) != "undefined" && typeof(serial_id) != "undefined" && typeof(car_id) != "undefined" && typeof(paramlist) != "undefined"){
        $.getJSON('http://price.auto.sina.cn/api/price/getCityLists?brand_id='+ brand_id +'&bid='+ bid +'&serial_id='+ serial_id +'&car_id='+ car_id, function(json) {
            if(json.status == 1){
                var data = json.data,
                    wholeAreas = data.cityList,
                    hotCities = data.hotCities,
                    lettersHTML = '',
                    recomHTML = '',
                    citiesHTML = '';
                for(var hotcity in hotCities){
                    var hPid = hotCities[hotcity].pid,
                        hCid = hotCities[hotcity].cid,
                        hName = hotCities[hotcity].name,
                        hUrl = '';
                    if(paramlist && paramlist != ''){
                        hUrl = 'http://db.auto.sina.com.cn/price/list' + paramlist + '-' + hPid + '-' + hCid + '-1' + '.html';
                    } else if(car_id != 0){
                        hUrl = 'http://db.auto.sina.com.cn/price/c' + car_id + '-' + hPid + '-' + hCid + '.html';
                    } else if(serial_id != 0){
                        hUrl = 'http://db.auto.sina.com.cn/price/s' + serial_id + '-' + hPid + '-' + hCid + '.html';
                    } else if(bid != 0){
                        hUrl = 'http://db.auto.sina.com.cn/price/p' + bid + '-' + hPid + '-' + hCid + '.html';
                    } else if(brand_id != 0){
                        hUrl = 'http://db.auto.sina.com.cn/price/b' + brand_id + '-' + hPid + '-' + hCid + '.html';
                    } else {
                        hUrl = 'http://db.auto.sina.com.cn/price' + '-' + hPid + '-' + hCid + '.html';
                    }
                    recomHTML += '<a href="'+ hUrl +'">'+ hName +'</a>';
                }
                for(var letter in wholeAreas){
                    var lName = letter,
                        provinceList = wholeAreas[letter],
                        dlHTML = '';
                    for(var province in provinceList){
                        var pId = provinceList[province].pid,
                            pName = provinceList[province].name,
                            cityList = provinceList[province].city_list,
                            ddHTML = '';
                        for(var city in cityList){
                            var cId = cityList[city].cid,
                                cName = cityList[city].name,
                                cUrl = '';
                            if(paramlist && paramlist != ''){
                                cUrl = 'http://db.auto.sina.com.cn/price/list' + paramlist + '-' + pId + '-' + cId + '-1' + '.html';
                            } else if(car_id != 0){
                                cUrl = 'http://db.auto.sina.com.cn/price/c' + car_id + '-' + pId + '-' + cId + '.html';
                            } else if(serial_id != 0){
                                cUrl = 'http://db.auto.sina.com.cn/price/s' + serial_id + '-' + pId + '-' + cId + '.html';
                            } else if(bid != 0){
                                cUrl = 'http://db.auto.sina.com.cn/price/p' + bid + '-' + pId + '-' + cId + '.html';
                            } else if(brand_id != 0){
                                cUrl = 'http://db.auto.sina.com.cn/price/b' + brand_id + '-' + pId + '-' + cId + '.html';
                            } else {
                                cUrl = 'http://db.auto.sina.com.cn/price' + '-' + pId + '-' + cId + '.html';
                            }
                            ddHTML += '<a href="'+ cUrl +'">'+ cName +'</a>';
                        }
                        dlHTML +=   '<dl class="clearfix">'
                               +        '<dt class="fL">'+ pName +'��</dt>'
                               +        '<dd class="fR">'
                               +            ddHTML
                               +        '</dd>'
                               +    '</dl>';
                    }
                    lettersHTML +=  '<a class="fL" data-name="'+ lName +'" href="javascript:void(0);">'+ lName +'</a>';
                    citiesHTML +=   '<li class="clearfix">'
                               +        '<p class="tit fL" data-name="'+ lName +'">'+ lName +'</p>'
                               +        '<div class="province fL">'
                               +            dlHTML
                               +        '</div>'
                               +    '</li>';
                }
                $('#J_cityLeters').html(lettersHTML);
                $('#J_cityList').find('.recom').html(recomHTML);
                $('#J_scrollCity').find('ul').html(citiesHTML);
            }
        });
    }
});