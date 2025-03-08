#include <node.h>
#include <v8.h>

using namespace v8;

void GetInt64FromBytes(const FunctionCallbackInfo<Value>& args) {
    if (!args[0]->IsUint8Array()) {
        args.GetReturnValue().Set(Nan::New("Invalid input").ToLocalChecked());
        return;
    }

    Local<Uint8Array> buffer = args[0].As<Uint8Array>();
    int64_t value = 0;
    for (int i = 0; i < 8; i++) {
        value = (value << 8) | buffer->Get(i)->Uint32Value();
    }

    args.GetReturnValue().Set(Nan::New<Number>(value));
}

void Initialize(Local<Object> exports) {
    NODE_SET_METHOD(exports, "getInt64FromBytes", GetInt64FromBytes);
}

NODE_MODULE(parser, Initialize);
