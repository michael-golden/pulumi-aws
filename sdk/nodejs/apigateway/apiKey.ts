// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";
import * as rxjs from "rxjs";
import * as operators from "rxjs/operators";

import {RestApi} from "./restApi";

/**
 * Provides an API Gateway API Key.
 * 
 * > **Warning:** Since the API Gateway usage plans feature was launched on August 11, 2016, usage plans are now **required** to associate an API key with an API stage.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const myDemoAPI = new aws.apigateway.RestApi("MyDemoAPI", {});
 * const myDemoDeployment = new aws.apigateway.Deployment("MyDemoDeployment", {
 *     restApi: myDemoAPI.id,
 *     stageName: "test",
 * });
 * const myDemoApiKey = new aws.apigateway.ApiKey("MyDemoApiKey", {
 *     stageKeys: [{
 *         restApi: myDemoAPI.id,
 *         stageName: myDemoDeployment.stageName,
 *     }],
 * });
 * ```
 */
export class ApiKey extends pulumi.CustomResource {
    /**
     * Get an existing ApiKey resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApiKeyState, opts?: pulumi.CustomResourceOptions): ApiKey {
        return new ApiKey(name, <any>state, { ...opts, id: id });
    }

    public static list(ctx: pulumi.query.ListContext, args?: pulumi.query.ListArgs): rxjs.Observable<ApiKeyResult> {
        return ctx.list({...args, type: 'aws:apigateway/apiKey:ApiKey'});
    }

    public static addAdmissionPolicy(policy: pulumi.policy.AdmissionPolicy): void {
        pulumi.runtime.addAdmissionPolicy({
            ...policy,
            pulumiType: 'aws:apigateway/apiKey:ApiKey',
        });
    }
    /**
     * The creation date of the API key
     */
    public /*out*/ readonly createdDate: pulumi.Output<string>;
    /**
     * The API key description. Defaults to "Managed by Terraform".
     */
    public readonly description: pulumi.Output<string>;
    /**
     * Specifies whether the API key can be used by callers. Defaults to `true`.
     */
    public readonly enabled: pulumi.Output<boolean | undefined>;
    /**
     * The last update date of the API key
     */
    public /*out*/ readonly lastUpdatedDate: pulumi.Output<string>;
    /**
     * The name of the API key
     */
    public readonly name: pulumi.Output<string>;
    /**
     * A list of stage keys associated with the API key - see below
     */
    public readonly stageKeys: pulumi.Output<{ restApi: RestApi, stageName: string }[] | undefined>;
    /**
     * The value of the API key. If not specified, it will be automatically generated by AWS on creation.
     */
    public readonly value: pulumi.Output<string>;

    /**
     * Create a ApiKey resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ApiKeyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ApiKeyArgs | ApiKeyState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ApiKeyState = argsOrState as ApiKeyState | undefined;
            inputs["createdDate"] = state ? state.createdDate : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["lastUpdatedDate"] = state ? state.lastUpdatedDate : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["stageKeys"] = state ? state.stageKeys : undefined;
            inputs["value"] = state ? state.value : undefined;
        } else {
            const args = argsOrState as ApiKeyArgs | undefined;
            inputs["description"] = (args ? args.description : undefined) || "Managed by Pulumi";
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["stageKeys"] = args ? args.stageKeys : undefined;
            inputs["value"] = args ? args.value : undefined;
            inputs["createdDate"] = undefined /*out*/;
            inputs["lastUpdatedDate"] = undefined /*out*/;
        }
        super("aws:apigateway/apiKey:ApiKey", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ApiKey resources.
 */
export interface ApiKeyState {
    /**
     * The creation date of the API key
     */
    readonly createdDate?: pulumi.Input<string>;
    /**
     * The API key description. Defaults to "Managed by Terraform".
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Specifies whether the API key can be used by callers. Defaults to `true`.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * The last update date of the API key
     */
    readonly lastUpdatedDate?: pulumi.Input<string>;
    /**
     * The name of the API key
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A list of stage keys associated with the API key - see below
     */
    readonly stageKeys?: pulumi.Input<pulumi.Input<{ restApi: pulumi.Input<RestApi>, stageName: pulumi.Input<string> }>[]>;
    /**
     * The value of the API key. If not specified, it will be automatically generated by AWS on creation.
     */
    readonly value?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ApiKey resource.
 */
export interface ApiKeyArgs {
    /**
     * The API key description. Defaults to "Managed by Terraform".
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Specifies whether the API key can be used by callers. Defaults to `true`.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * The name of the API key
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A list of stage keys associated with the API key - see below
     */
    readonly stageKeys?: pulumi.Input<pulumi.Input<{ restApi: pulumi.Input<RestApi>, stageName: pulumi.Input<string> }>[]>;
    /**
     * The value of the API key. If not specified, it will be automatically generated by AWS on creation.
     */
    readonly value?: pulumi.Input<string>;
}

/**
 * The live ApiKey resource.
 */
export interface ApiKeyResult {
    /**
     * The creation date of the API key
     */
    readonly createdDate: string;
    /**
     * The API key description. Defaults to "Managed by Terraform".
     */
    readonly description: string;
    /**
     * Specifies whether the API key can be used by callers. Defaults to `true`.
     */
    readonly enabled?: boolean;
    /**
     * The last update date of the API key
     */
    readonly lastUpdatedDate: string;
    /**
     * The name of the API key
     */
    readonly name: string;
    /**
     * A list of stage keys associated with the API key - see below
     */
    readonly stageKeys?: { restApi: RestApi, stageName: string }[];
    /**
     * The value of the API key. If not specified, it will be automatically generated by AWS on creation.
     */
    readonly value: string;
}
