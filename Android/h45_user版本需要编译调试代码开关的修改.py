"""
user root:
1:\system\core\adb\daemon\main.cpp
static bool should_drop_privileges() {
    // "adb root" not allowed, always drop privileges.
    //REMOVE if (!ALLOW_ADBD_ROOT && !is_device_unlocked()) return true;


    //REMOVE return drop;
	return false;//ADD
}

2:\system\core\init\init.cpp
static selinux_enforcing_status selinux_status_from_cmdline() {
/* REMOVE   selinux_enforcing_status status = SELINUX_ENFORCING;

    import_kernel_cmdline(false, [&](const std::string& key, const std::string& value, bool in_qemu) {
        if (key == "androidboot.selinux" && value == "permissive") {
            status = SELINUX_PERMISSIVE;
        }
    });

    return status;

	*/return SELINUX_PERMISSIVE;//ADD
}

static bool selinux_is_enforcing(void)
{
    if (ALLOW_PERMISSIVE_SELINUX) {
        return selinux_status_from_cmdline() == SELINUX_ENFORCING;
    }
//REMOVE    return true;
    return false;//ADD
}

3:\system\core\adb\services.cpp
void restart_root_service(int fd, void *cookie) {
    if (getuid() == 0) {
        WriteFdExactly(fd, "adbd is already running as root\n");
        adb_close(fd);
    } else {/* REMOVE
        if (!__android_log_is_debuggable()) {
            WriteFdExactly(fd, "adbd cannot run as root in production builds\n");
            adb_close(fd);
            return;
        }*/

        android::base::SetProperty("service.adb.root", "1");
        WriteFdExactly(fd, "restarting adbd as root\n");
        adb_close(fd);
    }
}


user ADB:
1:\system\core\adb\adbd_auth.cpp
bool auth_required = false;//true;

2:\device\qcom\i7s\i7s.mk
PRODUCT_DEFAULT_PROPERTY_OVERRIDES += persist.sys.usb.config=diag,serial_cdev,rmnet,dpl,adb

3:\system\core\adb\Android.mk
LOCAL_CFLAGS += -DALLOW_ADBD_ROOT=true
LOCAL_CFLAGS += -DALLOW_ADBD_NO_AUTH=true
LOCAL_CFLAGS += -DALLOW_ADBD_DISABLE_VERITY=1

user串口：
文件sdm710_i7s-perf_defconfig 中增加CONFIG_SERIAL_MSM_GENI_CONSOLE=y
"""